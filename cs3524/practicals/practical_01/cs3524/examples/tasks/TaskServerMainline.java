package cs3524.examples.tasks;

import java.rmi.Naming;
import java.rmi.RMISecurityManager;
import java.rmi.server.UnicastRemoteObject;

import java.net.InetAddress;

public class TaskServerMainline
{
  public static void main(String args[])
  {

    if (args.length < 2) {
      System.err.println( "Usage:\njava TaskServerMainline <registryport> <serverport>" ) ;
      return;
    }

    try
    {
      String hostname = (InetAddress.getLocalHost()).getCanonicalHostName() ;

      // specify at which port the rmiregistry is listening for binding and 
      // lookup requests

      int registryport = Integer.parseInt( args[0] ) ;

      // this is the port for our task service
      int serviceport = Integer.parseInt( args[1] );

      // We need to specify a security policy that gives the Java
      // Virtual Machine permission to contact DNS servers and 
      // interact with other JVMs via Internet protocols.
      // You can specify the policy at the command line using
      // -Djava.security.policy=thepolicyIwantyoutouse
      // Or within the program, thus:

      System.setProperty( "java.security.policy", "task.policy" ) ;
      System.setSecurityManager( new RMISecurityManager() ) ;

      // Incidentally, you can find out what system properties there
      // are in your JVM by doing this:
      // System.getProperties().list( System.out );

      // Generate the remote object(s) that will reside on this
      // server.

      ExecutionService taskservice = new ExecutionService();

      // export the task service to a specified port (our "service port") -
      // this is the port at which the remote object will be contacted
      // exporting the service will return the corresponding stub - this 
      // stub will be registered with rmiregistry

      ExecutionServiceInterface taskstub = 
        (ExecutionServiceInterface)UnicastRemoteObject.exportObject( taskservice, serviceport );

      // create a URL that uniquely identifies the registered service

      String regURL = "rmi://" + hostname + ":" + registryport + "/TaskService";

      System.out.println("Registering " + regURL );

      // Finally, register the stub of the remote object with the rmiregistry

      Naming.rebind( regURL, taskstub );

      // Note the server will not shut down!
    }
    catch(java.net.UnknownHostException e) {
      System.err.println( "Cannot get local host name." );
      System.err.println( e.getMessage() );
    }
    catch (java.io.IOException e) {
      System.err.println( "Failed to register." );
      System.err.println( e.getMessage() );
    }
  }
}

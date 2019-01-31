package cs3524.examples.sockets;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class ShoutClientSocket
{
  public ShoutClientSocket ( String hostname, int port) throws UnknownHostException, IOException, ClassNotFoundException
  {
    BufferedReader stdin = new BufferedReader( new InputStreamReader( System.in ));

    // Connect to and set up input/output streams with the server
    Socket server = new Socket( hostname, port );

    BufferedReader in  = new BufferedReader( new InputStreamReader( server.getInputStream() ) );
    PrintWriter    out = new PrintWriter( new OutputStreamWriter( server.getOutputStream() ), true );

    // read in the welcome message from the server
    System.out.println( in.readLine() );

    // start client
    System.out.print ( "ShoutClientSocket> " ) ;

    String message = stdin.readLine() ;

    out.println( message );
    //out.flush();

    message = in.readLine() ;

    System.out.println( "ShoutClientSocket> received message [" + message + "]" );

    server.close();
  }

  static public void main ( String args[] ) throws UnknownHostException, ClassNotFoundException, IOException
  {
    if (args.length < 2) {
      System.err.println( "Usage: java ShoutClientSocket <host> <port>" );
      return;
    }
    String hostname = args[0];
    int port = Integer.parseInt( args[1] );

    new ShoutClientSocket ( hostname, port ) ;
  }

}

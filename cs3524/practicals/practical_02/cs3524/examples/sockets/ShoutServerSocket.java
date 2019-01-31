package cs3524.examples.sockets;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class ShoutServerSocket
{
  public ShoutServerSocket ( int port) throws IOException, ClassNotFoundException
  {
    System.out.println ( "ShoutServerSocket: started, listening for client connect ..." ) ;
    ServerSocket listener = new ServerSocket(port);

    Socket client = listener.accept();
    System.out.println ( "ShoutServerSocket: client accepted") ;

    BufferedReader in  = new BufferedReader( new InputStreamReader( client.getInputStream() ) );
    PrintWriter    out = new PrintWriter( new OutputStreamWriter( client.getOutputStream() ), true );

    // send welcome message to connected client
    out.println( "Welcome to the socket-based ShoutServer" ) ;

    // receive message from client
    String message = in.readLine() ;
    System.out.println( "ShoutServerSocket: received message [" + message + "]" );

    // send message back to client
    out.println( message.toUpperCase() );

    System.out.println ( "ShoutServerSocket: finished." ) ;
    client.close();
    listener.close();
  }

  static public void main ( String args[] ) throws NumberFormatException, ClassNotFoundException, IOException
  {
    if (args.length != 1) {
      System.out.println("Usage: java ShoutServerSocket <port>");
      return;
    }
    new ShoutServerSocket(Integer.parseInt(args[0]));

  }

}

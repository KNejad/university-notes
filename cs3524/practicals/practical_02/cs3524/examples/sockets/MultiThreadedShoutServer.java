package cs3524.examples.sockets;

import java.io.IOException;
import java.io.PrintWriter;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;


public class MultiThreadedShoutServer
{
  public static void main( String args[] ) 
  {
    if (args.length < 1) {
      System.err.println( "Usage:\njava MultiThreadedShoutServer <port>" );
      return;
    }
    int port = Integer.parseInt( args[0] );

    try {
      ServerSocket listener = new ServerSocket( port );
      while (true)
        new ShoutServerConnection( listener.accept() ).start();
    }
    catch (Exception e) {
      e.printStackTrace( System.err );
    }
  }
}

class ShoutServerConnection extends Thread
{
  Socket _client;

  ShoutServerConnection( Socket client ) 
    throws SocketException
  {
    _client = client;
    setPriority( NORM_PRIORITY - 1 );
  }

  public void run()
  {
    try {
      BufferedReader in = new BufferedReader( new InputStreamReader( _client.getInputStream() ) );
      PrintWriter out = new PrintWriter( new OutputStreamWriter( _client.getOutputStream() ), true );
      out.println("Welcome to ShoutServer");
      String msg = in.readLine();
      msg = msg.toUpperCase();
      out.println(msg);
      _client.close();
    }
    catch ( IOException e ) {
      System.out.println( "I/O Error: " + e );
    }
  }
}

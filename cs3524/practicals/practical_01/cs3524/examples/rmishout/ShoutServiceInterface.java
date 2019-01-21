package cs3524.examples.rmishout;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ShoutServiceInterface extends Remote
{
  public String shout( String s ) throws RemoteException;
}

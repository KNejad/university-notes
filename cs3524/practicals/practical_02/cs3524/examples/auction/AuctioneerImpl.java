/*******************************************************************
 * cs3515.examples.auction.AuctioneerImpl                          *
 *******************************************************************/

package cs3524.examples.auction;

import java.rmi.RemoteException;
import java.util.Vector;
import java.util.Enumeration;


/**
 * An implementation of the AuctioneerInterface remote interface.

 * @see AuctioneerInterface

 * @author Tim Norman, University of Aberdeen
 * @version 1.0
 */

public class AuctioneerImpl
  implements AuctioneerInterface
{
  String _item;
  float _maxBid = -1;

  BidderInterface _winner = null;
  Vector _loosers = new Vector();


  /**
   * The constructor.  All that is required is to record the item
   * for sale.

   * @param item The item for sale at auction.
   */
  public AuctioneerImpl( String item, int auctionTime )
    throws RemoteException
  {
    _item = item;

    Thread thread = new Thread() {
      public void run(){
        try {
          Thread.currentThread().sleep(auctionTime);
        } catch (InterruptedException e) {
          System.out.println("Stop interrupting me");
        }
        callbackToBidders();
      }
    };

    thread.start();
  }

  /**
   * Method to handle a bid submitted for the item being auctioned.

   * This method is synchronized so that we ensure that the
   * auctioneer handles one bid at a time.

   * @param bidder A reference to the bidder submitting this bid for
   * call-back.
   * @param price The price bid for the item on sale.
   */
  public synchronized void getInfo(BidderInterface bidder) throws RemoteException
  {
    try {
      bidder.printInfo(_item, _maxBid);
    } catch (RemoteException e) {
      e.printStackTrace();
      System.exit(1);
    }
  }

  public synchronized void bid( BidderInterface bidder,
      float price )
    throws RemoteException
  {
    System.out.println( "New bid received = " + price );

    // If the new bid is equal to the current maximum bid, there
    // is a clash and both of these bidders become loosers.
    if (price == _maxBid) {

      System.out.println( "The new bid is the same as the current top bid." );

      _loosers.add( _winner );
      _loosers.add( bidder );
      _winner = null;
    }
    // If we have received a new top bid, replace the old top bid
    // with the new one, and record the new winner.
    if (price > _maxBid) {

      System.out.println( "The new bid is better than the current top bid." );

      if (_winner != null)
        _loosers.add( _winner );
      _winner = bidder;
      _maxBid = price;
    }
    // If the new bid received is lower that the current top bid,
    // this bidder is a looser.
    if (price < _maxBid) {

      System.out.println( "The new bid is worse than the current top bid." );

      _loosers.add( bidder );
    }
  }

  /**
   * Calls back to all bidders to inform them of the outcome of the
   * auction.
   */
  public void callbackToBidders()
  {
    try {
      String msg = "Item not sold.";
      // There may not be a winner, so we need to check that the
      // winner is not null.
      if (_winner != null) {
        _winner.won( _item, _maxBid );
        msg = "The item was sold for " + _maxBid + ".";
      }
      // Let all the others know that they have lost and inform them
      // of the outcome of the auction.
      for (Enumeration e = _loosers.elements() ; e.hasMoreElements() ;) {
        BidderInterface b = (BidderInterface)e.nextElement();
        if (b != null)
          b.lost( _item, msg );
      }
      System.out.println( "Clearing up references to bidders and resetting the auction..." );
      _maxBid = 0;
      _winner = null;
      _loosers.removeAllElements();
      System.out.println( "...done.  Please wait while the Java VM garbage collects.\n" +
          "Once this is done, the bidders should shut down.\n" +
          "Of course, you can force shutdown using ^C.\n" +
          "---------------------------------------------------------");
    }
    catch (RemoteException re) {
      System.err.println( "Failure to contact callback remote object." );
      re.printStackTrace( System.err );
    }
  }
}


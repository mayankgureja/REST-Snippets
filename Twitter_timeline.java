package twitter_timeline;

import twitter4j.*;
import java.util.List;

/**
 *
 * @author Mayank Gureja
 */
public class Twitter_timeline 
{

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        try 
        {
            // gets Twitter instance with default credentials
            Twitter twitter = new TwitterFactory().getInstance();
            User user = twitter.verifyCredentials();
            List<Status> statuses = twitter.getHomeTimeline();
            System.out.println("Showing @" + user.getScreenName() + "'s home timeline.");
            for (Status status : statuses) {
                System.out.println("@" + status.getUser().getScreenName() + " - " + status.getText());
            }
        } 
        catch (TwitterException te) 
        {
            te.printStackTrace();
            System.out.println("Failed to get timeline: " + te.getMessage());
            System.exit(-1);
        }
    }
}

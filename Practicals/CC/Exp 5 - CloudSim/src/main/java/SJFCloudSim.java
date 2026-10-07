import org.cloudsimplus.cloudlets.*;
import org.cloudsimplus.utilizationmodels.*;
import java.util.*;

public class SJFCloudSim {
    public static void main(String[] args) {
        var u = new UtilizationModelFull();
        List<Cloudlet> jobs = new ArrayList<>();
        long[] lengths = {40000, 10000, 30000, 20000};

        for(int i=0; i<lengths.length; i++) {
            Cloudlet c = new CloudletSimple(lengths[i], 1, u);
            c.setId(i);
            jobs.add(c);
        }

        System.out.println("Before SJF:");
        jobs.forEach(c -> System.out.println(c.getId()+" : "+c.getLength()));

        jobs.sort(Comparator.comparingLong(Cloudlet::getLength));

        System.out.println("\nAfter SJF:");
        jobs.forEach(c -> System.out.println(c.getId()+" : "+c.getLength()));
    }
}
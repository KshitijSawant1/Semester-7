## Experiment 5 — CloudSim with Custom SJF Scheduling

### Aim

To simulate cloud tasks using **CloudSim Plus** and implement a custom **Shortest Job First (SJF)** scheduling algorithm.

## A. macOS Steps

### 1. Install Java and Maven

```bash
brew install openjdk@17
brew install maven
```

Verify:

```bash
java -version
javac -version
mvn -version
```

### 2. Create Experiment Folder

```bash
cd "/Users/horizon/Programs/Semester 7/Practicals/CC"
mkdir -p "Exp 5 - CloudSim/src/main/java"
cd "Exp 5 - CloudSim"
```

### 3. Create `pom.xml`

```bash
nano pom.xml
```

Paste:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cloud</groupId>
    <artifactId>cloudsim-sjf</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.release>17</maven.compiler.release>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.cloudsimplus</groupId>
            <artifactId>cloudsim-plus</artifactId>
            <version>8.0.0</version>
        </dependency>
    </dependencies>
</project>
```

Save with **Ctrl + O → Enter → Ctrl + X**.

### 4. Create Java Program

```bash
nano src/main/java/SJFCloudSim.java
```

Paste:

```java
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
```

### 5. Compile

```bash
mvn clean compile
```

Expected:

```text
BUILD SUCCESS
```

### 6. Run

```bash
mvn exec:java -Dexec.mainClass="SJFCloudSim"
```

---

# B. Windows Steps

### 1. Install Requirements

Install:

- **JDK 17**
- **Apache Maven**

Then open **Command Prompt**:

```cmd
java -version
javac -version
mvn -version
```

All three commands should show their versions.

### 2. Create Experiment Folder

For example:

```cmd
cd C:\
mkdir "Exp 5 - CloudSim"
cd "Exp 5 - CloudSim"

mkdir src
mkdir src\main
mkdir src\main\java
```

Folder structure:

```text
Exp 5 - CloudSim
│
├── pom.xml
│
└── src
    └── main
        └── java
            └── SJFCloudSim.java
```

### 3. Create `pom.xml`

Run:

```cmd
notepad pom.xml
```

Paste the **same `pom.xml` code given above** and save it.

### 4. Create Java File

```cmd
notepad src\main\java\SJFCloudSim.java
```

Paste the **same Java program given above** and save.

### 5. Compile

Make sure Command Prompt is inside:

```text
C:\Exp 5 - CloudSim
```

Then:

```cmd
mvn clean compile
```

Expected:

```text
BUILD SUCCESS
```

### 6. Run

```cmd
mvn exec:java -Dexec.mainClass="SJFCloudSim"
```

---

## Expected Output on Both Windows and Mac

```text
Before SJF:
0 : 40000
1 : 10000
2 : 30000
3 : 20000

After SJF:
1 : 10000
3 : 20000
2 : 30000
0 : 40000
```

This shows:

```text
Original: 40000 → 10000 → 30000 → 20000

SJF:      10000 → 20000 → 30000 → 40000
```

The custom scheduling statement is:

```java
jobs.sort(Comparator.comparingLong(Cloudlet::getLength));
```

### Practical Procedure to Remember

**Windows:**

```text
Install JDK 17 + Maven
→ Create Exp 5 - CloudSim
→ Create pom.xml
→ Create SJFCloudSim.java
→ mvn clean compile
→ mvn exec:java -Dexec.mainClass="SJFCloudSim"
→ Check SJF output
```

**Mac:**

```text
brew install openjdk@17
→ brew install maven
→ Create Exp 5 - CloudSim
→ Create pom.xml
→ Create SJFCloudSim.java
→ mvn clean compile
→ mvn exec:java -Dexec.mainClass="SJFCloudSim"
→ Check SJF output
```

### Viva Points

**CloudSim:** A framework used for modeling and simulation of cloud computing environments.

**Cloudlet:** Represents a computational task/job in CloudSim.

**SJF:** Shortest Job First executes the job with the smallest task length first.

**Advantage:** Reduces average waiting time for shorter jobs.

**Disadvantage:** Longer jobs may suffer from starvation.

### Result

**Successfully used CloudSim Plus to model cloudlets and implemented a custom SJF scheduling policy that arranges cloudlets in ascending order of their computational length.**

## Experiment 8 — Install Hadoop Single-Node Cluster and Run WordCount

Here are the **proper start-to-end steps** you can keep for your practical.

### 1. Install Java

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
java -version
```

Find Java home:

```bash
dirname $(dirname $(readlink -f $(which java)))
```

### 2. Download Hadoop

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.4.2/hadoop-3.4.2.tar.gz
tar -xzf hadoop-3.4.2.tar.gz
mv hadoop-3.4.2 hadoop
```

### 3. Set Hadoop Environment

```bash
export HADOOP_HOME=$HOME/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

Configure Java:

```bash
nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```

Add:

```bash
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))
```

Save using **Ctrl+O → Enter → Ctrl+X**.

Verify:

```bash
hadoop version
```

Expected:

```text
Hadoop 3.4.2
```

### 4. Configure `core-site.xml`

```bash
nano $HADOOP_HOME/etc/hadoop/core-site.xml
```

Use:

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

Save and exit.

### 5. Configure `hdfs-site.xml`

```bash
nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

Use:

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

Save and exit.

### 6. Format the NameNode

Do this **only during initial setup**:

```bash
hdfs namenode -format
```

Look for a successful format message.

### 7. Configure SSH

```bash
sudo apt install openssh-server -y
```

Create SSH key:

```bash
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
```

Authorize it:

```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

Test:

```bash
ssh localhost
```

Enter:

```text
yes
```

Then return:

```bash
exit
```

### 8. Start Hadoop

```bash
start-dfs.sh
```

Check:

```bash
jps
```

You should see processes such as:

```text
NameNode
DataNode
SecondaryNameNode
Jps
```

### 9. Create WordCount Input

```bash
echo "hello hadoop hello cloud computing cloud" > input.txt
```

Create HDFS input directory:

```bash
hdfs dfs -mkdir -p /input
```

Upload the file:

```bash
hdfs dfs -put input.txt /input/
```

### 10. Run WordCount

```bash
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.2.jar wordcount /input /output
```

### 11. Display Result

```bash
hdfs dfs -cat /output/part-r-00000
```

Expected:

```text
cloud       2
computing   1
hadoop      1
hello       2
```

## Practical flow to remember

**Install Java → Download Hadoop → Set environment → Configure HDFS → Format NameNode → Configure SSH → Start HDFS → Create input → Run WordCount → View output**

### Result

> Hadoop single-node cluster was successfully installed and configured, and the WordCount MapReduce application was executed successfully.

For viva: **HDFS** stores distributed data, **NameNode** manages HDFS metadata, **DataNode** stores actual blocks, and **MapReduce** processes the data.

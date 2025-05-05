## HDFS commands
   
     we can write in two ways 
     1:hadoop fs ....
     2:hdfs dfs ....


     All command of linux will works but we need to provode absolute path 

     hadoop fs -linucCommand 
      cd is unkown command ...we can't change directory 


## copy /send data from local to hdfs

    hadoop fs -put  filename destination
              -copy from local  fileName destination   

     hadoop fs -head /user/kumar_abhishekpal23/test_file/file.text           
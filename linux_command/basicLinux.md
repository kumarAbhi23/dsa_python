 # Linux command for data engineering 

    clear : to clear every things from terminal 
    tab btn : for auto complete 
    touch filename : to create a folder/file...

    whoami : get infromation user who logged in 

 
  ### 1. Nevigation command 
       to navigate in between files 

       1.pwd: print working directory
          (needed to see excatly where you are right now)

         
           /home/kumar_abhishekpal23 

       2.cd :change directory  
         
         cd ~ : it will take to you home directory 

         cd folder_name(diretory): 
                   is same double clicking this folder 
        
         cd .. : to go back (just like back button)

         cd../.. : it will take me two pont back



    # directory struture 
     home->kumar_abhishekpal23/d1/d2...

     suppose i am at d1 and wanted to go d2
     1.absoulute path: full path from starting home 

             cd /home/kumar_abhishekpal123/d1/d2

     2.relative path : 
                 as i am at d1 i can go d2 easliy    

                 : cd d2     
                 
  
       3.ls command :
                for listing everything present in directory 


         ls :
             test_dir 
         ls -l:
              it will give more details about files with permission and type 

         kumar_abhishekpal23@cluster-ff00-m:~$ ls -l:

         total 4
         drwxr-xr-x 3 kumar_abhishekpal23 kumar_abhishekpal23 4096 May  3 13:37 test_dir  

         :4096- size in bytes 
         :kumar_abhishekpal23 -owner 
         :

         blue:folder/directory
         green:executable files
         black:normal files

         drwxr-xr-x 3 kumar_abhishekpal23 kumar_abhishekpal23 4096 May  3 13:37 test_dir
         -rwxr-xr-x 1 kumar_abhishekpal23 kumar_abhishekpal23    0 May  3 13:49 text.exe

         d: for directory 
         -: for file 

         ls -lt: all details with sorted with time (latest )
         ls -ltr: time reverse
         ls -a : to show hidden files also 


         --  i wanted to see all this in particluar directory without changing present direcotory 

         ls -R dirctoryName  : it wull directory and recusively go to folder also 

         kumar_abhishekpal23@cluster-ff00-m:~$ ls -R test_dir/
                                             test_dir/:
                                              d2
                                          test_dir/d2:

          ls -ltr -h: human readable 


## let see permissions in dir

      drwxr-xr-x 3 kumar_abhishekpal23 kumar_abhishekpal23 4096 May  3 13:37 test_dir

      d: directory 

      -rwxr-xr-x 1 kumar_abhishekpal23 kumar_abhishekpal23    0 May  3 13:49 text.exe

      -: files

      rwx       r-x      r-x 
      owner    group     other  (permission for desired groups)

      r-read       4
      w- write     2
      x-exetuble   1

      using chmod we can change permission 
      chmod 444  test.exe - read only 
      chmod 777 text.exe  - all permission 
      chmod 666  ....    -read and write 
      chmod 766 ....    -all for owner,r and w for group and others


   ## File operation 
       move : to move file ...cut file
       remove: to delete file 
       copy   : normal copy 

       Move file : mv fileName finalLocation
       kumar_abhishekpal23@cluster-ff00-m:~/test_dir$ mv localFile d2

       remnaming 
       mv test.exe renamed_test.exe

       delete file /directory 
        rm test2.exe
        rm -r directoryName
        rm -f filename: force delete 

        Copy 
        cp souce destination 
        cp file.text d2   but meta data not preseved : time and other 
        cp  -p file.txt d : here meta data preseved 



## file edit operations 
     vi fileNmae   : enter inside file 
     i : to enter insert mode 

     
     esc - to exit from insert mode
     :w -save
     :q -quit
     :wq -save and quit
     :q! quit without saving

     

      head fileNme :retun 10 lines 
     head -n 5 fileNme : return first 5 lines 
     tail fileName: retunr 

     cat filetxt : show all file content 
## Search and Pattern Matching 
    
    grep 1 file.text : we are searching 1 in file.text


    https://allthingdata.substack.com/p/essential-linux-commands-for-data


    list data by name 
    ls -ltr *Fi*: * is any thing we can use either side alos 
      



      



         






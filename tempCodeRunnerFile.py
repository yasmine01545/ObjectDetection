while 1:
   ret, img = cap.read()
   if not ret:
      print("no frame captured")
      exit()

   img = cv2.resize(img,(1280,720))
   #continue processing
   classIds,confs,bbox=net.detect(img,confThreshold=0.5)
   print(classIds,bbox)


   if len(classIds)!=0:
        
                    
                for classId,confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                    cv2.rectangle(img,box,color=(0,250,0),thickness=2)
                    
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                            cv2.FONT_HERSHEY_COMPLEX,1,(0,250,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    
   cv2.imshow("Outout",img)
   cv2.waitKey(1)











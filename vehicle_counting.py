import cv2
import glob
from vehicle_detector import VehicleDetector

#create empty list
vehicleCountList=[]

# Load Veichle Detector
vd = VehicleDetector()


# Load images from a folder
images_folder = glob.glob("images/*.jpg")

vehicles_folder_count = 0
#creating dictionary 



# Loop through all the images
for img_path in images_folder:
    print("Img path", img_path)
    img = cv2.imread(img_path)
    img = cv2.resize(img,(1000,1000))


    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)
    
  
    vehicleCountList.append(vehicle_count)

    # Update total count
    vehicles_folder_count += vehicle_count

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    cv2.imshow("Cars", img)
    cv2.waitKey(0)

print("Total current count", vehicles_folder_count) 
print (vehicleCountList[0])
print (vehicleCountList[1])
v1 = vehicleCountList[0]
v2 = vehicleCountList[1]

print('STATUS OF THE LIGHT')
if v1>v2:
  print('priority given to',v1)
   
  
   
    
   
     
else:
    print('priority is given to',v2)
       
   





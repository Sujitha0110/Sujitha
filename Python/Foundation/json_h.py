import json

stds={
      1:{
            
      }
}

# to load and display data
with open(r"C:\Users\AnudipCOA\Desktop\file_handling\std.data.json","a") as j_file:
    # student=json.load(j_file)
    #   student=json.dumps(stds)
      student=json.dumps(stds,j_file,indent=2)
      print(student)
    # print(student["marks"]["Python"])






























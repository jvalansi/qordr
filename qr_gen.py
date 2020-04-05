#! /usr/bin/env python
import os
import MyQR.myqr as myqr
import uuid

base_url = 'http://qordr.com/qrcode/'
outdir = 'qrs'
num_of_ids = 10
num_of_qrs_per_id = 10

for i in range(num_of_ids):
     myID = uuid.uuid4()
     print(myID)
     save_dir = os.path.join(outdir, str(myID))
     os.mkdir(save_dir)
     for j in range(num_of_qrs_per_id):
         ver, ecl, qr_name = myqr.run(base_url+str(myID)+'/'+str(i),
                                      save_dir=save_dir,
                                      save_name=str(j)+'.png')

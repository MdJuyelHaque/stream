#Author "Md Juyel Haque"
from time import sleep
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import pymongo
import flatten_json
from encrypt import *
task='Test.TestDB.dbo.Test'
connection=mongoconect
database=db
#consumer
consumer = KafkaConsumer(task,bootstrap_servers=['localhost:9092'],value_deserializer=lambda x:json.loads(x.decode('utf-8')),auto_offset_reset='latest', enable_auto_commit=True,group_id="test1")
message=None
table_name=None
payload=None
list1=[]
doc1=0
def task_insert_merge():
    for message in consumer:
        message = message.value
        payload=message['after']
        print(payload)
        mongoclient = pymongo.MongoClient(connection)
        db = mongoclient[database]
        print("The original dictionary : " + str(payload))
        res = {key: payload[key] for key in payload.keys()
                                & {'UnitOfWorkId','TaskId','BuildingName','TaskStagePickingTypeId'}}
        
        print(res)
        taskid = list(res.keys())[1]
        unitofworkid= list(res.keys())[0]
        print(taskid)
        print(unitofworkid)
        print(res["UnitOfWorkId"])
        task= res["TaskId"]
        unitof=res["UnitOfWorkId"]   
        buildingname=res["BuildingName"] 
        db.juyel_test.update_many({'TaskId':res["TaskId"]},{"$set":payload},upsert=True)
        
        
        col = db["UnitOfWork"]
        
        query =col.find({"UnitOfWorkId":res["UnitOfWorkId"]},{'_id':0})   
        for document in query:
            doc={key: document[key] for key in document.keys() & {'UnitOfWorkId'}}
            print(document)     
            print(doc)  
            db.juyel_test.update_many({'TaskId':res["TaskId"]},{"$set": document},upsert=True)     
            
        u_col = db["UnitOfWork"]
        u_query =u_col.find({"UnitOfWorkId":res["UnitOfWorkId"]},{'_id':0})   
        for document in u_query:
            u_doc={key: document[key] for key in document.keys() & {'WorkQueueId'}}
            print(document)     
            print(u_doc)   
            
        w_col = db["WorkQueue"]
        w_query =w_col.find({"WorkQueueId":u_doc["WorkQueueId"]},{'_id':0})   
        for w_document in w_query:
            w_doc={key: w_document[key] for key in w_document.keys() & {'WorkQueueId'}}
            print(w_document)     
            print(w_doc)   
            db.juyel_test.update_many({'TaskId':res["TaskId"]}, {"$set": w_document},upsert=True)     
        
        ulu_col = db["UnitOfWorkLastPickedByUser"]
        ulu_query =ulu_col.find({"UnitOfWorkId":res["UnitOfWorkId"]},{'_id':0})   
        for ulu_document in ulu_query:
            ulu_doc={key: ulu_document[key] for key in ulu_document.keys() & {'UnitOfWorkId'}}
            print(ulu_document)     
            print(ulu_doc)   
            db.juyel_test.update_many({'TaskId':res["TaskId"]}, {"$set": ulu_document},upsert=True)   
        ua_col = db["UnitOfWorkTaskAggregate"]
        ua_query =ua_col.find({"UnitOfWorkId":res["UnitOfWorkId"]},{'_id':0})   
        for ua_document in ua_query:
            ua_doc={key: ua_document[key] for key in ua_document.keys() & {'UnitOfWorkId'}}
            print(ua_document)     
            print(ua_doc)  
            db.juyel_test.update_many({'TaskId':res["TaskId"]}, {"$set": ua_document},upsert=True) 
            
        bcode_col = db["BuildingPriorityCode"]
        bcode_query =bcode_col.find_one({},{'_id':0})  
        print(bcode_query) 
        db.juyel_test.update_many({'TaskId':res["TaskId"]}, {"$set": bcode_query},upsert=True)
        taskp_col = db["TaskStagePickingType"]
        taskp_query =taskp_col.find({"TaskStagePickingTypeId":res["TaskStagePickingTypeId"]},{'_id':0})   
        for taskp_document in taskp_query:
            taskp_doc={key: taskp_document[key] for key in taskp_document.keys() & {'TaskStagePickingTypeId'}}
            print(taskp_document)     
            print(taskp_doc)   
            db.juyel_test.update_many({'TaskId':res["TaskId"]}, {"$set": taskp_document},upsert=True)
            
        assign_col = db["Assignment"]
        assign_query =assign_col.find({"UnitOfWorkId":res["UnitOfWorkId"]},{'_id':0})   
        print(assign_query)
        for assign_document in assign_query:
            assign_doc={key: assign_document[key] for key in assign_document.keys() & {'AssignmentId'}}
            print(assign_document)     
            print(assign_doc)   
            db.juyel_test.update_many({'TaskId':res["TaskId"]}, {"$set": assign_document},upsert=True)
        
task_insert_merge()
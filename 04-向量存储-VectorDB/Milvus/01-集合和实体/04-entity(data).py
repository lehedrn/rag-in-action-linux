from gc import collect
from pymilvus import MilvusClient
import random

from sympy import limit

# 连接到 Milvus
client = MilvusClient(
    uri="http://localhost:19530",
    token="root:Milvus"
)


def create_collection(collection_name):
    # 1. 创建集合
    # 检查集合是否存在，如果存在则删除
    if client.has_collection(collection_name):
        client.drop_collection(collection_name)

    # 创建集合
    client.create_collection(
        collection_name=collection_name,
        dimension=5,  # vector 维度
        primary_field_name="id",
        vector_field_name="vector",
        id_type="int"
    )
    print(f"集合 {collection_name} 创建成功")


def insert_data(collection_name):
    # 2. 插入实体
    data=[
        {"id": 0, "vector": [0.3580376395471989, -0.6023495712049978, 0.18414012509913835, -0.26286205330961354, 0.9029438446296592], "color": "pink_8682"},
        {"id": 1, "vector": [0.19886812562848388, 0.06023560599112088, 0.6976963061752597, 0.2614474506242501, 0.838729485096104], "color": "red_7025"},
        {"id": 2, "vector": [0.43742130801983836, -0.5597502546264526, 0.6457887650909682, 0.7894058910881185, 0.20785793220625592], "color": "orange_6781"},
        {"id": 3, "vector": [0.3172005263489739, 0.9719044792798428, -0.36981146090600725, -0.4860894583077995, 0.95791889146345], "color": "pink_9298"},
        {"id": 4, "vector": [0.4452349528804562, -0.8757026943054742, 0.8220779437047674, 0.46406290649483184, 0.30337481143159106], "color": "red_4794"},
        {"id": 5, "vector": [0.985825131989184, -0.8144651566660419, 0.6299267002202009, 0.1206906911183383, -0.1446277761879955], "color": "yellow_4222"},
        {"id": 6, "vector": [0.8371977790571115, -0.015764369584852833, -0.31062937026679327, -0.562666951622192, -0.8984947637863987], "color": "red_9392"},
        {"id": 7, "vector": [-0.33445148015177995, -0.2567135004164067, 0.8987539745369246, 0.9402995886420709, 0.5378064918413052], "color": "grey_8510"},
        {"id": 8, "vector": [0.39524717779832685, 0.4000257286739164, -0.5890507376891594, -0.8650502298996872, -0.6140360785406336], "color": "white_9381"},
        {"id": 9, "vector": [0.5718280481994695, 0.24070317428066512, -0.3737913482606834, -0.06726932177492717, -0.6980531615588608], "color": "purple_4976"}
    ]

    res = client.insert(
        collection_name=collection_name,
        data=data
    )

    print(res)

def update_data(collection_name):
    # 3. 更新实体
    update_data = [
        {"id": 0, "vector": [random.random() for _ in range(5)], "color": "updated_pink_8682"},
        {"id": 1, "vector": [random.random() for _ in range(5)], "color": "updated_red_7025"}
    ]

    res = client.upsert(
        collection_name=collection_name,
        data=update_data
    )
    print("\n更新结果:", res)

def query_data(collection_name):
    # 4. 查询实体
    res = client.query(
        collection_name=collection_name,
        filter="id in [1,2]",
        # limit=10,
        output_fields=["id", "color"]
    )
    print("\n查询结果:", res)

def delete_data(collection_name):
    # 5. 删除实体
    res = client.delete(
        collection_name=collection_name,
        ids=[0]
    )
    print("\n删除结果:", res)

if __name__ == "__main__":
    
    collection_name = "quick_setup"
    
    # create_collection(collection_name)
    # insert_data(collection_name)
    # update_data(collection_name)
    # query_data(collection_name)
    delete_data(collection_name)

    # 6. 清理
    client.drop_collection(collection_name)
    print(f"集合 {collection_name} 已删除")

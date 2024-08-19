## Get All Materials

**URL:**

`GET /api/materials`

**Response** (list format):

```json
{
    "code": 200,
    "message": Success,
    "data": [
        {
            "id": 1,
            "code": "JK099",
            "name": "Kain Blaco Jamaika",
            "type": "jeans",
            "buy_price": 150.0,
            "produsen_id": [
                1,
                "Jadi Makmur"
            ]
        },
        {
            "id": 3,
            "code": "C001",
            "name": "Kapas",
            "type": "cotton",
            "buy_price": 130.0,
            "produsen_id": [
                1,
                "Jadi Makmur"
            ]
        },
...
    ]
}
```

## Create Material

**URL:**  
`POST /api/materials`

**Request Body** (in dictionary format):

```json
{
    "params": {
        "code": "<MATERIAL_CODE>",
        "name": "<MATERIAL_NAME>",
        "type": "<MATERIAL_TYPE>",
        "buy_price": "<BUY_PRICE>",
        "produsen_id": "<SUPPLIER_ID>"
    }
}

**Response:**

```json
{
    "jsonrpc": "2.0",
    "id": null,
    "result": "<Response 78 bytes [200 OK]>"
}
```

## Update Material

**URL:**  
`PUT /api/materials/<MATERIAL_ID>`

**Request Body** (fields to be updated):

```json
{
    "params": {
        "code": "<MATERIAL_CODE>",
        "name": "<MATERIAL_NAME>",
        "type": "<MATERIAL_TYPE>",
        "buy_price": "<BUY_PRICE>",
        "produsen_id": "<PRODUSEN_ID>"
    }
}

**Responses:**

- **Successful update:**

```json
{
    "jsonrpc": "2.0",
    "id": null,
    "result": "<Response 65 bytes [200 OK]>"
}
```

## Delete Material

**URL:** 
`DELETE /api/materials/<MATERIAL_ID>`

**Responses:**

```json
{
    "code": 200,
    "message": Hapus Material berhasil!,
    "data": None
}
```


## Get All Produsen

**URL:**

`GET /api/produsen`

**Response** (list format):

```json
{
    "code": 200,
    "message": Success,
    "data": [
        {
            "id": 1,
            "name": "Jadi Makmur",
            "contact": "0274 3800xx"
        },
        {
            "id": 2,
            "name": "Cotton Collect",
            "contact": "0274 230xxx"
        }
    ]
}
```
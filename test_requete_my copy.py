from pydoc import cli
from urllib import response
import requests
import webbrowser, os, json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

url = 'https://my.tikee.io/v2/graphql'

headers = {
    'API_ACCESS_TOKEN': '5c1ebd45d91c9b5b1c01eff2ceda7314',
    'Content-Type': 'application/json',
}

transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport)

query = gql("""query Tikee($id: Int!) {  tikee(id: $id) {    id    uuid    serialNumber    sdFreeSpace    uploadState    lastFirmwareVersion    statusUploadedAt    tikeeLocation    mcuFirmwareRevision    mobileLocation    monthlySmsSendingCount    simPhoneNumber    wakeUpOnDemandAction    wakeUpOnDemandCalledAt    geolocation    energySaver    isUpdated    uploadMode    uploadModeThreshold    tzOffset    wakeUpOnDemandVideoSensor    wakeUpOnDemandCalledAt    ...CapabilityValues    ...NetworkQuality    ...LteConnectionInfos    ...LongSequences    ...ShortSequences    ...LastSequence    ...RollingStatus    ...AlwaysOnTriggers    __typename  }}""")

params = {"id": 6009}

response = client.execute(query, variable_values=params)

for key in response['tikee'].keys():
    print(key)
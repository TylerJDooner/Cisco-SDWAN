import requests
import json
from datetime import datetime
from ensdwiauth import getAuth
from ensdwidevices import getDevices
from ensdwievents import getEvents
from ensdwiomppeers import getOMPpeers
from ensdwicontrolconn import getControlConnections
from ensdwitunnelstats import getTunnelStats
from datetimehandler import epochHandler, epochFormatter, epochTableFormatter
from prettytable import PrettyTable
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://192.168.254.107/"

if __name__ == "__main__":
    # Get Authenticated

    sesh = getAuth(base_url, 'admin', 'tyler')

    # Get device data
    devices = getDevices(base_url, sesh)

    # set up table
    deviceTable = PrettyTable(['Hostname', 'Site', 'Sys-ID', 'Status'])

    # retrieve each device's details
    for device in devices['data']:
        deviceTable.add_row([device['host-name'], device['site-id'],
                             device['system-ip'], device['status']])
    print(deviceTable)

    # Get events in the last 24 hours
    events = getEvents(base_url, sesh)
    eventTable = PrettyTable(
        ['Hostname', 'Event', 'Sys-ID', 'Component', 'Severity', 'EventTime'])
    for event in events['data']:
        datediff = epochHandler(event['entry_time'])
        if datediff < 24:
            entrytime = epochTableFormatter(event['entry_time'])
            eventTable.add_row([event['host_name'], event['eventname'],
                                event['vmanage_system_ip'], event['component'], event['severity_level'], entrytime])
    print(eventTable)

    # get device control connections
    device_id = '7.7.7.10'
    controlconnections = getControlConnections(base_url, sesh, device_id)

    controltable = PrettyTable(
        ['hostname', 'system-ip', 'site', 'peer', 'color', 'protocol', 'uptime'])

    for control in controlconnections['data']:
        controltable.add_row([control['vdevice-host-name'], control['system-ip'], control['site-id'],
                              control['peer-type'], control['local-color'], control['protocol'], control['uptime']])
    print(controltable)


    # get device tunnel statistics
    device_id = '7.7.7.10'
    tunnelstats = getTunnelStats(base_url, sesh, device_id)
    tunneltable = PrettyTable(['hostname', 'source color', 'remote color',
                               'source ip', 'dest ip', 'tx packets', 'rx packets'])
    for stat in tunnelstats['data']:
        tunneltable.add_row([stat['vdevice-host-name'], stat['local-color'], stat['remote-color'],
                             stat['source-ip'], stat['dest-ip'], stat['tx_pkts'], stat['rx_pkts']])

    print(tunneltable)

    # Get omp data
    device_id = '7.7.7.20'
    omp = getOMPpeers(base_url, sesh, device_id)

    # set up table
    ompTable = PrettyTable(['Name', 'Site ID', 'Hostname', 'state', 'Uptime', 'Peer', 'Type'])

    # retrieve each omp peer's details
    for peer in omp['data']:
        uptime = peer.get('uptime', 'N/A')
        ompTable.add_row([peer['vdevice-name'], peer['site-id'], peer['vdevice-host-name'], peer['state'], peer['up-time'], peer['peer'], peer['type']])
                        
        

    print(ompTable)

    
import requests
import json
from datetime import datetime
from ensdwiIPSECout import getIPSECout
from ensdwiauth import getAuth
from ensdwidevices import getDevices
from ensdwiomppeers import getOMPpeers
from ensdwicontrolconn import getControlConnections
from ensdwiIPSECout import getIPSECout
from ensdwiOMPRoutesReceived import getOMProutes
from ensdwiBFDsessions import getBFDsession
from ensdwiTLOCroutes import getTLOCroutes
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
    print("Device Table")
    print(deviceTable)

   

    # get device control connections
    device_id = '7.7.7.10'
    controlconnections = getControlConnections(base_url, sesh, device_id)

    controltable = PrettyTable(
        ['hostname', 'system-ip', 'site', 'peer', 'color', 'protocol', 'uptime'])

    print("Control Connections")
    for control in controlconnections['data']:
        controltable.add_row([control['vdevice-host-name'], control['system-ip'], control['site-id'],
                              control['peer-type'], control['local-color'], control['protocol'], control['uptime']])
        print(controltable)
   

    # Get omp data
    device_id = '7.7.7.10'
    omp = getOMPpeers(base_url, sesh, device_id)

    # set up table
    ompTable = PrettyTable(['Name', 'Site ID', 'Hostname', 'state', 'Uptime', 'Peer', 'Type'])

    # retrieve each omp peer's details
    print("OMP Peers")
    for peer in omp['data']:
        uptime = peer.get('uptime', 'N/A')
        ompTable.add_row([peer['vdevice-name'], peer['site-id'], peer['vdevice-host-name'], peer['state'], peer['up-time'], peer['peer'], peer['type']])
    print(ompTable)

        
    # # Get IPSEC Outbound data to specific tunnel
    # device_id = '7.7.7.10'
    # remote_address = '7.7.7.40'
    # remote_color = 'mpls'

    # ipsec_Outbound = getIPSECout(base_url, sesh, device_id, remote_address, remote_color)
    # #print(type(ipsec_Outbound))

    # # set up table
    # ipsecoutTable = PrettyTable(['Dest IP', 'Integrity', 'Local Device', 'Remote Device', 'Source IP'])

    # # retrieve each omp peer's details
    # print("IPSEC Outbound connections")
    # for tunnel in ipsec_Outbound['data']:
    #     ipsecoutTable.add_row([tunnel['dest-ip'], tunnel['ip-udp-esp'], tunnel['vdevice-name'], tunnel['remote-tloc-address'], tunnel['source-ip']])
    # print(ipsecoutTable)

    # Get BFD Session data
    device_id = '7.7.7.10'
    

    bfd_Sessions = getBFDsession(base_url, sesh, device_id)
    

    # set up table
    bfdTable = PrettyTable(['Source IP', 'Destination IP', 'Color', 'Local Device', 'Remote System IP', 'Site-ID' , 'vEdge Host Name', 'Local Color', 'Uptime', 'State'])

    # retrieve each omp peer's details
    print("BFD Sessions")
    for bfd in bfd_Sessions['data']:
        bfdTable.add_row([bfd['src-ip'], bfd['dst-ip'], bfd['color'], bfd['vdevice-name'], bfd['system-ip'], bfd['site-id'], bfd['vdevice-host-name'], 
                          bfd['local-color'], bfd['uptime'], bfd['state']])
    print(bfdTable)



# Get IPSEC Outbound data
    device_id = '7.7.7.10'
    

    ipsec_Outbound = getIPSECout(base_url, sesh, device_id)
    #print(type(ipsec_Outbound))

    # set up table
    ipsecoutTable = PrettyTable(['Dest IP', 'Integrity', 'Local Device', 'Remote Device', 'Source IP'])

    # retrieve each omp peer's details
    print("IPSEC Outbound connections")
    for tunnel in ipsec_Outbound['data']:
        ipsecoutTable.add_row([tunnel['dest-ip'], tunnel['integrity-used'], tunnel['vdevice-name'], tunnel['remote-tloc-address'], tunnel['source-ip']])
    print(ipsecoutTable)



    # Get TLOC data
    device_id = '7.7.7.10'
    

    tloc_ROUTES = getTLOCroutes(base_url, sesh, device_id)
    

    # set up table
    tlocRouteTable = PrettyTable(['BFD Status', 'Color', 'vEdge', 'Remote System IP', 'From Peer', 'Encap', 'site-id', 'originator', 'TLOC Public IP', 'TLOC Private IP'])

    # retrieve BFD status
    print("BFD status")
    for tloc in tloc_ROUTES['data']:
        tlocRouteTable.add_row([tloc['bfd-status'], tloc['color'], tloc['vdevice-name'], tloc['ip'], tloc['from-peer'], tloc['encap'], tloc['site-id'], tloc['originator'],
                               tloc['tloc-public-ip'], tloc['tloc-private-ip']])
    print(tlocRouteTable)




    # Get OMP Route data
    device_id = '7.7.7.10'
    

    omp_all_ROUTES = getOMProutes(base_url, sesh, device_id)
    #print(type(ipsec_Outbound))

    # set up table
    ompRouteTable = PrettyTable(['color', 'vEdge', 'prefix', 'Remote System IP', 'From Peer', 'label', 'site-id', 'originator', 'VPN-ID', 'Protocol', 'Status'])

    # retrieve each omp peer's details
    print("OMP Routes Received")
    for route in omp_all_ROUTES['data']:
        ompRouteTable.add_row([route['color'], route['vdevice-name'], route['prefix'], route['ip'], route['from-peer'], route['label'], route['site-id'], route['originator'],
                               route['vpn-id'], route['protocol'], route['status']])
    print(ompRouteTable)

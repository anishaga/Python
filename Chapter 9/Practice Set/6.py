# with open("E:/Python/Chapter 9/Practice Set/log.txt","w") as f:
#     f.write(''' 03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP
# 03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp
# 03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP
# 03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp
# 03/22 08:51:06 TRACE  :..entity_initialize: interface 127.0.0.1, entity for rsvp allocated and initialized
# 03/22 08:51:06 INFO   :......mailslot_create: creating socket for querying route
# 03/22 08:51:06 INFO   :.....mailbox_register: no mailbox necessary for forward
# 03/22 08:51:06 INFO   :......mailslot_create: creating mailslot for route engine - informational socket
# 03/22 08:51:06 TRACE  :......mailslot_create: ready to accept informational socket connection
# 03/22 08:51:11 INFO   :.....mailbox_register: mailbox allocated for route
# 03/22 08:51:11 INFO   :.....mailslot_create: creating socket for traffic control module
# 03/22 08:51:11 INFO   :....mailbox_register: no mailbox necessary for traffic-control
# 03/22 08:51:11 INFO   :....mailslot_create: creating mailslot for RSVP client API
# 03/22 08:51:11 INFO   :...mailbox_register: mailbox allocated for rsvp-api
# 03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for terminate
# 03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for terminate
# 03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for dump
# 03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for dump
# 03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for (broken) pipe
# 03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for pipe
#  07 
# 03/22 08:51:11 INFO   :.main: rsvpd initialization complete
#  08 
# 03/22 08:52:50 INFO   :......rsvp_api_open: accepted a new connection for rapi
# 03/22 08:52:50 INFO   :.......mailbox_register: mailbox allocated for mailbox
# 03/22 08:52:50 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 does not exist
#  09 
# 03/22 08:52:50 EVENT  :.....api_reader: api request SESSION
#  10 
# 03/22 08:52:50 TRACE  :......rsvp_event_establishSession: local node will send
# 03/22 08:52:50 INFO   :........router_forward_getOI: Ioctl to get route entry successful
# 03/22 08:52:50 TRACE  :........router_forward_getOI:         source address:   9.67.116.98
# 03/22 08:52:50 TRACE  :........router_forward_getOI:         out inf:   9.67.116.98
# 03/22 08:52:50 TRACE  :........router_forward_getOI:         gateway:   0.0.0.0
# 03/22 08:52:50 TRACE  :........router_forward_getOI:         route handle:   7f5251c8
#  11 
# 03/22 08:52:50 TRACE  :.......event_establishSessionSend: found outgoing if=9.67.116.98 through 
# forward engine
# 03/22 08:52:50 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists
#  12 
# 03/22 08:52:50 EVENT  :.....api_reader: api request SENDER
#  13 
# 03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  Entering
 
# 03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  papiLogFunc = 98681F0 papiUserValue = 0
 
# 03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  Exiting
 
# 03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  Entering
 
# 03/22 08:52:50 INFO   :.......init_policyAPI: open_socket:  Entering
 
# 03/22 08:52:50 INFO   :.......init_policyAPI: open_socket:  Exiting
 
# 03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  ApiHandle = 98BDFB0,  connfd = 22
 
# 03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  Exiting
 
# 03/22 08:52:50 INFO   :.......init_policyAPI: RegisterWithPolicyAPI:  Entering ''')

with open("E:/Python/Chapter 9/Practice Set/log.txt","r") as f:
    data = f.read().lower()

if "python" in data:
    print("python is present")
else:
    print("python is not present")

data = [row for row in open('sample_input.txt').read().split('\n')]

# message = '8A004A801A8002F478'
message = 'A0016C880162017C3686B18A3D4780'

packet_stack = ['{0:08b}'.format(int(message, 16)).zfill(len(message) * 4)]

version_sum = 0

while len(packet_stack) > 0:
  packet = packet_stack.pop()  
  version = int(packet[:3], 2)
  type_id = int(packet[3:6], 2)
  
  
  if type_id == 4:
    print(packet)
    print('Version: {} | Type ID: {}'.format(version, type_id))
    
  else:
    length_type_id = int(packet[6:7], 2)
    sub_packets = ''
    if length_type_id == 0:
      sub_packets_length = int(packet[7:22], 2) if length_type_id == 0 else 0
      sub_packets = packet[22:22+sub_packets_length]

    elif length_type_id == 1:
      sub_packets_count = int(packet[7:18], 2) if length_type_id == 1 else 0

    sub_packets = packet[22:22+sub_packets_length] if length_type_id == 0 else packet[18:]
    if sub_packets_length > 0:
      spl = 0
      while spl < sub_packets_length:
        new_packet = ''
        sp_version = int(sub_packets[:3], 2)
        sp_type_id = int(sub_packets[3:6], 2)
    elif sub_packets_count > 0:
      pass

    packet_stack.append(sub_packets)

    print(packet)
    print('Version: {} | Type ID: {} | Length Type ID: {}'.format(version, type_id, length_type_id))

  version_sum += version

print(version_sum)
  
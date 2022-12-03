data = [row for row in open('sample_input.txt').read().split('\n')]

# message = '38006F45291200'
message = 'EE00D40C823060'


class Message():
  def __init__(self, message):
    self.message = message
    self.binary_message = '{0:08b}'.format(int(message, 16)).zfill(len(message) * 4)    
    self.version = int(self.binary_message[:3], 2)
    self.type_id = int(self.binary_message[3:6], 2)
    self.length_type_id = int(self.binary_message[6:7], 2) if self.type_id != 4 else None
    self.sub_packets_length = int(self.binary_message[7:22], 2) if self.length_type_id == 0 else None
    self.sub_packets_count = int(self.binary_message[7:18], 2) if self.length_type_id == 1 else None

    if self.sub_packets_length != None:
      self.sub_packets = self.binary_message[22:22+self.sub_packets_length]
    elif self.sub_packets_count != None:
      self.sub_packets = self.binary_message[18:]
    else:
      self.sub_packets = None

  def __repr__(self):
    return 'Version: {} | Type ID: {} | Length Type ID: {} | Sub Packets Length: {} | Sub Packets Count: {}'.format(
      self.version,
      self.type_id,
      self.length_type_id,
      self.sub_packets_length,
      self.sub_packets_count
    )





new_message = Message(message)

print(new_message.message)
print(new_message)
print(new_message.binary_message)
print('VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB')
print(new_message.sub_packets)

  

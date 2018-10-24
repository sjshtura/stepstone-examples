
def csv_to_dict(fh, delimiter = ' '):

	my_dict = {}

	header_line = fh.readline()
	headers = header_line.rstrip().split(delimiter)
	_, *keys = tuple(headers)

	for line in fh:
		data_list = line.rstrip().split(delimiter)
		name, *data = tuple(data_list)
		line_data = dict(zip(keys, data))
		my_dict[name] = line_data

	return my_dict



fh = open('bundeslaender.txt','r', encoding='ISO-8859-1')
laender_dict = csv_to_dict(fh)
print(laender_dict)
fh.close()

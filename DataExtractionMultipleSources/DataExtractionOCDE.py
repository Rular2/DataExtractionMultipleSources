from cif import cif
data, subjects, measures = cif.createDataFrameFromOECD(countries = ['USA'],dsname = 'MEI', frequency = 'M')
print(data, "|", subjects, "|", measures)


from RootFile import RootFile
import uproot

fileobject = open('sample_root1.root')
fileobject.seek(0,2)
size = fileobject.tell()
fileobject.close()

rootfile = RootFile('sample_root1.root')
rootfile.setSize(size)



# rootfile.setName('sample_root1.root')
# rootfile.extractMetadata()
# rootfile = uproot.open('sample_root1.root')
# print(dir(rootfile))
# tree = rootfile['Events']
# # print(tree.keys())
# branch = tree['EventAuxiliary']
# print(branch._fBasketBytes)
# print(branch._fBasketEntry)
# print(branch._fBasketSeek)
# print(branch._fBasketSize)
# print(dir(branch))
# print(branch._fBasketSize)
# print(branch._fBaskets)
# print(branch.keys())
# print(branch.allitems())

rootfile.extractMetadata()
file = open('test.txt','w')
rootfile.save(file)
file.close()

rootfile = RootFile()
file = open('test.txt','r')
rootfile.restore(file)
file.close()




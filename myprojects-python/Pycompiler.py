import py_compile
infilename = raw_input("Enter the infile name :")
print infilename
outfilename = infilename+'c'
py_compile.compile(infilename,cfile = outfilename)

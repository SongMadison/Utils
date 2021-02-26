sudo apt-get install -y libexpat1-dev  #(required for Parser)
cpan XML::Parser
cpan XML::DOM
pip install boto3

#use latest version 
pip install -U git+https://github.com/pltrdy/pyrouge
Git clone https://github.com/bheinzerling/pyrouge.git


git clone https://github.com/pltrdy/files2rouge.git     
cd files2rouge
python setup_rouge.py
python setup.py install




#error1:  when running "python setup_rouge.py"
-- This error is not important

files2rouge uses scripts and tools that will not be stored with the python package
where do you want to save it? [default: /home/azureuser/.files2rouge/]
Copying './files2rouge/RELEASE-1.5.5/' to '/home/azureuser/.files2rouge/'
Traceback (most recent call last):
  File "setup_rouge.py", line 40, in <module>
    data = copy_rouge()
  File "setup_rouge.py", line 33, in copy_rouge
    shutil.copytree(src_rouge_root, path)
  File "/anaconda/lib/python3.7/shutil.py", line 359, in copytree
    raise Error(errors)
shutil.Error: [('./files2rouge/RELEASE-1.5.5/data/smart_common_words.txt', 
'/home/azureuser/.files2rouge/data/smart_common_words.txt', 
"[Errno 38] Function not implemented: './files2rouge/RELEASE-1.5.5/data/smart_common_words.txt'"),
 ('./files2rouge/RELEASE-1.5.5/data/WordNet-1.6-Exceptions/adj.exc', '/home/azureuser/.files2rouge/data/WordNet-1.6-Exceptions/adj.exc', "[Errno 38] Function not implemented: './files2rouge/RELEASE-1.5.5/data/WordNet-1.6-Exceptions/adj.exc'"), ('./files2rouge/RELEASE-1.5.5/data/WordNet-1.6-Exceptions/adv.exc', '/home/azureuser/.files2rouge/data/WordNet-1.6-Exceptions/adv.exc', "[Errno 38] Function not implemented: './files2rouge/RELEASE-1.5.5/data/WordNet-1.6-Exceptions/adv.exc'"), ('./files2rouge/RELEASE-1.5.5/data/WordNet-1.6-Exceptions/buildExeptionDB.pl', '/home/azureuser/.files2rouge/data/WordNet-1.6-Exceptions/buildExeptionDB.pl', "[Errno 38] Function not implemented: './files2rouge/RELEASE-1.5.5/data/WordNet-1.6-Exceptions/buildExeptionDB.pl'"),

# https://bugs.python.org/issue24564
# https://stackoverflow.com/questions/51616058/shutil-copystat-fails-inside-docker-on-azure/51635427#51635427
The issues is about copy data using shutil.copytree between two file sytesms


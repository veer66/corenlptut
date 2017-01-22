# สาธิตการใช้ CoreNLP เบื้องต้น

## สิ่งที่ต้องการก่อนติดตั้ง

1. Java VM
2. curl
3. BASH

## การติดตั้ง

1. ดาวโหลด CoreNLP http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip
2. unzip stanford-corenlp-full-2016-10-31.zip


## เริ่มให้ server ทำงาน

1. cd stanford-corenlp-full-2016-10-31/
2. สั่ง

      java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

3. เปิดหน้าต่างที่รัน server ทิ้งไว้ โดยจะเห็นความทำนองนี้

      $ java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
      [main] INFO CoreNLP - --- StanfordCoreNLPServer#main() called ---
      [main] INFO CoreNLP - setting default constituency parser
      [main] INFO CoreNLP - warning: cannot find edu/stanford/nlp/models/srparser/englishSR.ser.gz
      [main] INFO CoreNLP - using: edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz instead
      [main] INFO CoreNLP - to use shift reduce parser download English models jar from:
      [main] INFO CoreNLP - http://stanfordnlp.github.io/CoreNLP/download.html
      [main] INFO CoreNLP -     Threads: 4
      [main] INFO CoreNLP - Starting server...
      [main] INFO CoreNLP - StanfordCoreNLPServer listening at /0:0:0:0:0:0:0:0:


## ใช้งาน CoreNLP

1. ในอีกหน้าต่างหนึ่งสั่งคำสั่งนี้

      curl --data 'The quick brown fox jumped over the lazy dog.' 'http://localhost:9000/?properties={%22annotators%22%3A%22tokenize%2Cssplit%2Cpos%22%2C%22outputFormat%22%3A%22json%22}' -o -

จะได้ผลลัพธ์ตามด้านล่าง

      $ curl --data 'The quick brown fox jumped over the lazy dog.' 'http://localhost:9000/?properties={%22annotators%22%3A%22tokenize%2Cssplit%2Cpos%22%2C%22outputFormat%22%3A%22json%22}' -o -

      {"sentences":[{"index":0,"tokens":[{"index":1,"word":"The","originalText":"The","characterOffsetBegin":0,"characterOffsetEnd":3,"pos":"DT","before":"","after":" "},{"index":2,"word":"quick","originalText":"quick","characterOffsetBegin":4,"characterOffsetEnd":9,"pos":"JJ","before":" ","after":" "},{"index":3,"word":"brown","originalText":"brown","characterOffsetBegin":10,"characterOffsetEnd":15,"pos":"JJ","before":" ","after":" "},{"index":4,"word":"fox","originalText":"fox","characterOffsetBegin":16,"characterOffsetEnd":19,"pos":"NN","before":" ","after":" "},{"index":5,"word":"jumped","originalText":"jumped","characterOffsetBegin":20,"characterOffsetEnd":26,"pos":"VBD","before":" ","after":" "},{"index":6,"word":"over","originalText":"over","characterOffsetBegin":27,"characterOffsetEnd":31,"pos":"IN","before":" ","after":" "},{"index":7,"word":"the","originalText":"the","characterOffsetBegin":32,"characterOffsetEnd":35,"pos":"DT","before":" ","after":" "},{"index":8,"word":"lazy","originalText":"lazy","characterOffsetBegin":36,"characterOffsetEnd":40,"pos":"JJ","before":" ","after":" "},{"index":9,"word":"dog","originalText":"dog","characterOffsetBegin":41,"characterOffsetEnd":44,"pos":"NN","before":" ","after":""},{"index":10,"word":".","originalText":".","characterOffsetBegin":44,"characterOffsetEnd":45,"pos":".","before":"","after":""}]}]}$ 
$ 

     
ดาวโหลดจาก
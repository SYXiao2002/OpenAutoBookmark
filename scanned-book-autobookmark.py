import PyPDF2

# 打开PDF文件
pdf_file = open('scanned-book.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# 创建一个新的PDF文档对象
output_pdf = PyPDF2.PdfFileWriter()

# 打开bookmark.txt文件并读取内容
with open('scanned-book-manual-toc.txt', 'r') as f:
    lines = f.readlines()

# 校正页码的偏移量
page_offset = 27

# 初始化章节计数器
chapter_count = 1

# 遍历bookmark.txt中的每一行
for line in lines:
    # 解析章节标题和内容页码
    chapter_title, content_page = line.strip().split(' ')
    content_page = int(content_page) + page_offset - 2

    # 在章节标题前添加章节index
    chapter_title_with_index = f'Chapter {chapter_count}: {chapter_title}'

    # 将新书签添加到输出PDF中
    output_pdf.addBookmark(title=chapter_title_with_index, pagenum=content_page)

    # 增加章节计数器
    chapter_count += 1

# 将原始PDF文件的内容复制到输出PDF中，并写入到新文件中
for i in range(pdf_reader.getNumPages()):
    output_pdf.addPage(pdf_reader.getPage(i))
output_file = open('scanned-book_with_bookmarks.pdf', 'wb')
output_pdf.write(output_file)

# 关闭文件对象
pdf_file.close()
output_file.close()

import pdfrw


# pdf = pdfrw.PdfReader()

# for page in pdf.pages:
#     page.MediaBox.UpperLeft = (0, 0)
#     page.MediaBox.LowerRight = (500, 500)
    # # 获取页面的所有图像对象。
    # images = page.getImages()
    # # 遍历图像对象列表。
    # for image in images:
    #     # 将图像对象的颜色模式设置为黑白。
    #     image.colorspace = pdfrw.PdfColorspace.GRAY

writer = pdfrw.PdfWriter(compress=True)

pages = pdfrw.PdfReader('Interchange Intro-Student book.pdf').pages

for page in pages[13:21]:
    writer.addPage(page)

writer.write('output.pdf')
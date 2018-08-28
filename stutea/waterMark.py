from PIL import Image,ImageDraw,ImageFont
im=Image.open("1.jpg").convert("PNG")
# img1 = Image.new("RGBA",im.size,(0,0,0,0))
# font=ImageFont.truetype("arial.ttf",35)
#
# fontsize=font.getsize("handsome It's mine")
#
# draw = ImageDraw.Draw(img1)
# draw.text(((im.size[0]-fontsize[0])/2,(im.size[1]-fontsize[1])/2),"handsome It's mine",fill=(254,254,254),font=font)
# im=Image.alpha_composite(im,img1)
im.show()


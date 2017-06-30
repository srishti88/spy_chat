from steganography.steganography import Steganography
in_image = "brave.jpg"
out_image = "brave2.jpg"
message = "no artist tolerates reality"
Steganography.encode(in_image,out_image,message)

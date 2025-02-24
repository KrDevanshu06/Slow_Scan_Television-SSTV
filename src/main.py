import argparse
import soundfile as sf
from src.utils.image import load_image, save_image

def main():
    parser = argparse.ArgumentParser(description="SSTV Encoder/Decoder")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Encoder subcommand
    encode_parser = subparsers.add_parser("encode", help="Encode image to SSTV audio")
    encode_parser.add_argument("--image", required=True, help="Path to input image")
    encode_parser.add_argument("--mode", default="martin_m1", choices=["martin_m1", "scottie_s1"], help="SSTV mode")
    encode_parser.add_argument("--output", required=True, help="Path to output audio file")
    
    # Decoder subcommand
    decode_parser = subparsers.add_parser("decode", help="Decode SSTV audio to image")
    decode_parser.add_argument("--audio", required=True, help="Path to input audio file")
    decode_parser.add_argument("--output", required=True, help="Path to output image file")
    
    args = parser.parse_args()
    
    if args.command == "encode":
        from src.encoder import encode_image_to_audio
        
        # For simplicity, we use fixed dimensions
        image = load_image(args.image, width=320, height=256)
        audio_signal = encode_image_to_audio(image, mode=args.mode)
        sf.write(args.output, audio_signal, 44100)
        print(f"Encoded image saved to {args.output}")
    
    elif args.command == "decode":
        from src.decoder import decode_audio_to_image
        
        image_array = decode_audio_to_image(args.audio)
        save_image(image_array, args.output)
        print(f"Decoded image saved to {args.output}")

if __name__ == "__main__":
    main()

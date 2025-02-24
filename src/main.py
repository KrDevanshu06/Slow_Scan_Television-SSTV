import argparse
import soundfile as sf

def main():
    parser = argparse.ArgumentParser(description="SSTV Encoder/Decoder")
    parser.add_argument("--mode", choices=["encode", "decode"], required=True, help="Operation mode: encode or decode")
    parser.add_argument("--input", required=True, help="Input file path (image for encode, audio for decode)")
    parser.add_argument("--output", required=True, help="Output file path (audio for encode, image for decode)")
    parser.add_argument("--sstv_mode", choices=["martin_m1", "scottie_s1"], default="martin_m1", help="SSTV mode to use")
    args = parser.parse_args()

    if args.mode == "encode":
        from utils.image import load_image
        from encoder import encode_image_to_audio

        # Load image and encode
        image = load_image(args.input, width=320, height=256)
        audio_signal = encode_image_to_audio(image)
        sf.write(args.output, audio_signal, 44100)
        print(f"Encoded image saved to {args.output}")

    elif args.mode == "decode":
        from decoder import decode_audio_to_image
        from utils.image import save_image

        # Decode audio to image (stub implementation)
        image_array = decode_audio_to_image(args.input)
        save_image(image_array, args.output)
        print(f"Decoded image saved to {args.output}")

if __name__ == "__main__":
    main()

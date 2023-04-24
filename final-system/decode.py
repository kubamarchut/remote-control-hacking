verbose = False
n = 4

def decode(signal):
    signal_divided = [signal[i:i+n] for i in range(0, len(signal), n)]

    # słownik
    decoding = {
        "1000" : "0",
        "1110" : "1"
    }

    received_code = ""

    for sign in signal_divided:
        if not sign in decoding:
            print("error", sign)
        else:
            received_code += decoding[sign]

    if verbose: print(received_code)

    dec_code = int(received_code, 2)

    if verbose: print(dec_code)

    return dec_code

if __name__ == "__main__":
    print("atempting internal module test")
    signal = "100010001000111010001110100010001000111010001110100011101000111010001000111011101000100011101110"
    print("passing sample data")

    decoded_signal = decode(signal)

    if decoded_signal == 1332531:
        print("Test passed. Signal succesfully decoded.")
        print("Output:", decoded_signal)
    
    
    signal2 = ['100010001000111010001110100010001000111010001110100011101000111011101110100010001000100011101110', '010001000010001110100011110100010001000111101000111010001111010001110111001110100010001000010001', '100010001000111010001110100010001000111010001110100011101000111011101110100010001000100011101110', '010001000110001110100011101100010001000111011000111010001110110001110111011101100010001000100001', '100010001000111010001110100010001000111010001110100011101000111011101110100010001000100011101110', '010001100010001110100011100100010001000111101000111010001111010001110111001110100010001100010001', '100010001000111010001110100010001000111010001110100011101000111011101110110011001000110011111110', '010001100010001110100011110100010001100011101000111011000111010001111011101110100011000100010001', '100010001000111010001110100010001000111010001110100011101000111011101110100010001000100011101110', '010001000110001110100011101100010001000111011000111010001110110001110111011100100010001000100001', '100010001000111010001110110011001000111111000111010001110100011101110111010001000100010001110111', '010001100010001110110011110100010001000011101000111001000111010001111011101110100011000100010001', '100010001000111010001110100010001000111010001110100011101000111011101110100010001000100011101110', '010001000110001110100011101100010001000111011000111010001110010001110111011101100010001000100001', '100010001000111010001110100010001000111010001110100011101000111011101110100010001000100011101110', '010001100010001110100011110100010001000111101000111010000111010001110111001110100010001100010001']
    for signal in signal2:
        decoded_signal2 = decode(signal)

        if decoded_signal2 != 1332531:
            print("Test passed. Signal succesfully decoded.")
            print("Output:", decoded_signal2)
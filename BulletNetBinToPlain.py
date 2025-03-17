import os
import struct

# Define network architecture dimensions for a perspective NNUE
input_size = 768  # Input vector length
hidden_size = 128  # Hidden layer size
output_size = 1  # Scalar output


def read_raw_bin(path):
    """
    Reads a binary file containing quantized weights and returns a list of int16 values.
    Assumes little-endian encoding with 2 bytes per weight.

    Args:
        path (str): Path to the binary file.

    Returns:
        list: List of weights as integers.
    """
    with open(path, 'rb') as file:
        data = file.read()
    return [struct.unpack('<h', data[i:i + 2])[0] for i in range(0, len(data), 2)]


def save_weights_to_txt(weights, output_path):
    """
    Saves the full list of weights to a plain text file.
    If the file exists, it is cleared before writing.

    Args:
        weights (list): List of weights.
        output_path (str): Output file path.
    """
    with open(output_path, 'w') as file:
        file.writelines(f"{weight}\n" for weight in weights)


def save_to_file(filename, weights):
    """
    Writes a list of weights to a file inside the 'output' directory.
    If the file already exists, it is overwritten.

    Args:
        filename (str): Name of the output file.
        weights (list): List of weights to write.
    """
    os.makedirs("output", exist_ok=True)
    file_path = os.path.join("output", filename)
    with open(file_path, "w") as file:
        file.writelines(f"{weight}\n" for weight in weights)


def write_data_to_bc_format(weights):
    """
    Splits the flat list of weights into sections for a perspective NNUE network.

    Expected parameters for a perspective network:
      - H (input-to-hidden weights): input_size * hidden_size
      - b (hidden bias): hidden_size
      - O (output weights): 2 * hidden_size   (two sets, one per perspective)
      - c (output bias): output_size (1)

    Total expected count = (768*128) + 128 + (2*128) + 1 = 98,689.
    """
    # Calculate expected sizes for each section
    h_size = input_size * hidden_size  # Weights H
    b_size = hidden_size  # Bias b
    o_size = 2 * hidden_size  # Output weights O (for both perspectives)
    c_size = output_size  # Output bias c

    expected_total = h_size + b_size + o_size + c_size

    # Trim extra values (if padded) or warn if too few
    if len(weights) > expected_total:
        print(f"Trimming {len(weights) - expected_total} extra padded weights.")
        weights = weights[:expected_total]
    elif len(weights) < expected_total:
        print(f"Warning: Expected {expected_total} weights, but only found {len(weights)}.")

    # Split the weights list using dynamic indices
    idx = 0
    H = weights[idx: idx + h_size]
    idx += h_size
    b = weights[idx: idx + b_size]
    idx += b_size
    O = weights[idx: idx + o_size]
    idx += o_size
    c = weights[idx: idx + c_size]
    idx += c_size

    # Optional verification
    print("Parameter counts:")
    print("Input-to-hidden (H):", len(H))
    print("Hidden bias (b):", len(b))
    print("Output weights (O):", len(O))
    print("Output bias (c):", len(c))

    # Save each section to its respective text file
    save_to_file("NN_Input_to_Hidden_Weights.txt", H)
    save_to_file("NN_Hidden_Bias.txt", b)
    save_to_file("NN_Output_Weights.txt", O)
    save_to_file("NN_Output_Bias.txt", c)


def main():
    # Ensure the output directory exists
    os.makedirs("output", exist_ok=True)

    bin_path = "bin/quantised.bin"  # Path to the quantized binary file
    full_output_path = os.path.join("output", "all_values_translated_res.txt")  # Full weight dump file

    # Read and convert the binary file to a list of weights
    weights = read_raw_bin(bin_path)

    # Save the complete list of weights to a plain text file (overwriting if it exists)
    save_weights_to_txt(weights, full_output_path)

    # Split the weights based on the network architecture and save each section
    write_data_to_bc_format(weights)

    print(f"Conversion complete. Full weights saved to {full_output_path}")


if __name__ == "__main__":
    main()

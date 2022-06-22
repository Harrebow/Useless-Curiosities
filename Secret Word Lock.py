blocks = int(input("Enter the number of blocks: "))
blocks_left = blocks

i = -1
layer = 0

while blocks_left > layer:
    blocks_left = blocks_left + i
    count = (i - (i*2))
    i -= 1
    layer += 1
    blocks_used = blocks - blocks_left
    print("\nLayer:", layer, "\nNumber of blocks in layer", layer, "is:", count, "\nTotal blocks used so far:", blocks_used, "\nBlocks left:", blocks_left)
    blocks_used = blocks - blocks_left

height = layer
print("\n-- The height of the pyramid:", height, "--\n-- Remaining blocks:", blocks_left, "--")
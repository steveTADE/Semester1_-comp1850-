from image import Image
import perlin_noise, time

grid_size = 512
weights = [0] * (grid_size * grid_size)
perlin = perlin_noise.PerlinNoise()
perlin.octaves = 2.5


def self_made_bucket_sort(weights : list, preset_limit : int) -> list:
    length             = len(weights)
    output             = [0] * length        # this is for the output
    tmp                = [0] * (preset_limit + 1)  # this is for sorting it
    index              = 0
    incrementing_index = 0
    for value in weights:   # this kinda sort then
        tmp[value] += 1
    #breakpoint()
    while incrementing_index < (preset_limit + 1):
        tmp_num = tmp[incrementing_index]
        #print(incrementing_index, tmp_num) #debug line
        if tmp_num == 0:
            incrementing_index += 1
            continue
        for _i in range(tmp_num):
            output[index] = incrementing_index
            index += 1
        incrementing_index += 1
    return output

def bucket_sort(weights: list, preset_limit: int) -> list:
    output = [0] * len(weights)
    tmp = [0] * (preset_limit + 1)

    for value in weights:
        tmp[value] += 1

    index = 0

    for value, count in enumerate(tmp):
        if count:
            output[index:index + count] = [value] * count
            index += count

    return output

for row in range(grid_size):
    for col in range(grid_size):
        weights[row * grid_size + col] = abs(int(255 * (perlin.noise([row / grid_size, col / grid_size]))))
#debug lines
print("Minimum:", min(weights))
print("Maximum:", max(weights))
print("Negative values:", sum(1 for x in weights if x < 0))

start         = time.time()
tmp_output_1  = bucket_sort(weights, grid_size)
end           = time.time()
timed_tmp_1   = end - start
start         = time.time()
tmp_output_2  = sorted(weights)
end           = time.time()
timed_tmp2    = end - start
if tmp_output_1 == tmp_output_2:
    print(timed_tmp2, timed_tmp_1)
    #exit()
#for row in range(grid_size):
#    for col in range(grid_size):
#        weights[row * grid_size + col] = grid_size - (row - col)

#print(weights)
img = Image().create(grid_size, grid_size, weights)
img.write_pgm("stuff.pgm")
mirror_img = Image().create(grid_size, grid_size, tmp_output_1)
mirror_img.write_pgm("mirrored_stuff.pgm")

#new_image = Image.copy("/workspaces/Semester1_-comp1850-/week1.6/session2/images/coins.pgm")
#Image.write_pgm(img, new_image)
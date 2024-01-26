Figure out how to use this yourself I forgot how xd

## Solve 1
You can brute force check_x on every square since it doesn't reset even if you get on a mine. Otherwise you can find that the mine/flag generation is seeded with the current time.

## Solve 2
Multiple ways to rev the logic, but basically the secret code is stored in memory rotated by +1. You can just reverse the rotation and get the code, input it, and get the flag in console.

#!/usr/bin/node
if (process.argv[2]) {
  for (let outer = 0; outer < process.argv[2]; outer++) {
    for (let inner = 0; inner < process.argv[2]; inner++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}

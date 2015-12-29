main:main.f
	./compiler.py main.f main
	cp main /Users/mnolan/programming/asm/stack_cpu/emulator/stack_emulator/main
clean:
	rm main

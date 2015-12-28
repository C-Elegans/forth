main:main.s
	stack_as main.s main
	cp main /Users/mnolan/programming/asm/stack_cpu/emulator/stack_emulator/main
main.s:main.f
	./compiler.py main.f main.s
clean:
	rm main.s main

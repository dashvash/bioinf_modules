# bioinf_modules
Модуль с двумя функциями для работы с последовательностями нуклеиновых кислот. 

## Описание функций
### run_dna_rna_tools
Функция принимает на вход произвольное количество аргументов с последовательностями ДНК или РНК (str), а также название процедуры которую нужно выполнить последним агрументом. После этого она делает заданное действие над всеми переданными последовательностями и возвращает результат.

#### Доступные процедуры
* **transcribe** — вернуть транскрибированную последовательность
* **reverse** — вернуть развёрнутую последовательность
* **complement** — вернуть комплементарную последовательность
* **reverse_complement** — вернуть обратную комплементарную последовательность

#### Пример использования
    run_dna_rna_tools('ATG', 'transcribe') -> 'AUG'
    run_dna_rna_tools('ATG', 'reverse') -> 'GTA'
    run_dna_rna_tools('AtG', 'complement') -> 'TaC'
    run_dna_rna_tools('ATg', 'reverse_complement') -> 'cAT'
    run_dna_rna_tools('ATG', 'aT', 'reverse') -> ['GTA', 'Ta']

### filter_fastq




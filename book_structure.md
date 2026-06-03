# Структура книги

Терминология:
- часть --- \addpart{PartName}
- глава --- \chapter
- раздел --- \section
- подраздел --- \subsection
- Вводная часть главы --- то, что идёт до начала первого раздела.
- Вводная часть раздела --- то, что идёт до начала первого подраздела.


Условные обозначения статусов:
- ✅ — раздел полностью написан
- ⚠️ — раздел присутствует частично или требует доработки
- ❌ — содержание раздела отсутствует, есть только заготовка

Статус главы: ✅ (все разделы ✅) | ⚠️ (есть хотя бы один ⚠️ или ❌) | ❌ (все разделы ❌)


---

## Правила структурирования и именования файлов

Все исходники лежат в директории `tex/`.

### Общие правила
1. Все имена файлов и директорий — только латиница.
2. **Часть** — директория `part_NN_Name/`. Содержит `main.tex` (`\addpart` + вводная часть части + `\input` глав) и поддиректории глав.
3. **Глава** — директория `chapter_NN_Name/` внутри своей части. Содержит `main.tex` (`\chapter` + вводная часть главы + `\input` разделов) и файлы разделов. Если глава не разбита на разделы, `main.tex` содержит всё.
4. **Раздел** — файл `NN_Name.tex` рядом с `main.tex` главы. Содержит `\section{...}` и всё наполнение, включая вложенные подразделы (`\subsection`).
5. **Подразделы в отдельные файлы не выносятся и отдельных директорий не имеют.**
6. **Изображения** — в директории `figures/` внутри директории главы. Если рисунков много, группируются в поддиректории, названные по номеру раздела: `figures/03_TensorProduct/`, `figures/05_BottomUp/LR0/` и т.п.
7. Техническая директория `figures/externalized/` — `tex/figures/externalized/`.
8. `styles/` — настройки отдельных пакетов и вспомогательный функции.

### Frontmatter
- Файлы: `Introduction.tex` и `List_of_contributors.tex` — в директории `frontmatter/`.

### Пример
```
tex/
└── part_02_Foundations/
    ├── main.tex
    └── chapter_05_RegularLanguages/
        ├── main.tex
        ├── 01_RegularExpressions.tex
        ├── 02_FiniteAutomata.tex
        ├── ...
        └── figures/
```

---

## Соответствие старых файлов новым

### Frontmatter и корень

| Старый файл                | Новый файл                             |
| -------------------------- | -------------------------------------- |
| `Introduction.tex`         | `frontmatter/Introduction.tex`         |
| `List_of_contributors.tex` | `frontmatter/List_of_contributors.tex` |

### Часть 1. Предподготовка

| Старый файл            | Новый файл                                                                  |
| ---------------------- | --------------------------------------------------------------------------- |
| *— не существует*      | `part_01_Prep/main.tex`                                                     |
| `LinearAlgebra.tex`    | `part_01_Prep/chapter_01_LinearAlgebra/main.tex` — *разбивается на разделы* |
| ↳                      | `01_BinaryOperations.tex`                                                   |
| ↳                      | `02_Semigroup.tex`                                                          |
| ↳                      | `03_Monoid.tex`                                                             |
| ↳                      | `04_Group.tex`                                                              |
| ↳                      | `05_Semiring.tex`                                                           |
| ↳                      | `06_Ring.tex`                                                               |
| ↳                      | `07_MatricesAndVectors.tex`                                                 |
| ↳                      | `08_AppliedAspects.tex`                                                     |
| `SetTheory.tex`        | `part_01_Prep/chapter_02_SetTheory/main.tex` — *разбивается*                |
| ↳                      | `01_BasicDefinitions.tex`                                                   |
| ↳                      | `02_Relations.tex`                                                          |
| `GraphTheoryIntro.tex` | `part_01_Prep/chapter_03_GraphTheoryIntro/main.tex` — *разбивается*         |
| ↳                      | `01_BasicDefinitions.tex`                                                   |
| ↳                      | `02_PathProblems.tex`                                                       |
| ↳                      | `03_PathAlgebra.tex`                                                        |
| ↳                      | `04_BFS.tex`                                                                |
| `figures/graph/*`      | `part_01_Prep/chapter_03_GraphTheoryIntro/figures/`                         |

### Часть 2. Подготовка

| Старый файл                           | Новый файл                                                                          |
| ------------------------------------- | ----------------------------------------------------------------------------------- |
| *— не существует*                     | `part_02_Foundations/main.tex`                                                      |
| `FormalLanguageTheoryIntro.tex`       | `part_02_Foundations/chapter_04_FormalLanguageTheoryIntro/main.tex` — *разбивается* |
| ↳                                     | `01_SetOperations.tex`                                                              |
| ↳                                     | `02_Derivatives.tex`                                                                |
| ↳                                     | `03_Recognizers.tex`                                                                |
| ↳                                     | `04_Generators.tex`                                                                 |
| ↳                                     | `05_LanguageClasses.tex`                                                            |
| `RegularLanguages.tex`                | `part_02_Foundations/chapter_05_RegularLanguages/main.tex` — *разбивается*          |
| ↳                                     | `01_RegularExpressions.tex`                                                         |
| ↳                                     | `02_FiniteAutomata.tex`                                                             |
| ↳                                     | `03_DerivativesForRegex.tex`                                                        |
| ↳                                     | `04_RegexToFA.tex`                                                                  |
| ↳                                     | `05_FAToRegex.tex`                                                                  |
| ↳                                     | `06_LinearGrammars.tex`                                                             |
| ↳                                     | `07_PumpingLemma.tex`                                                               |
| ↳                                     | `08_ClosureProperties.tex`                                                          |
| `Context-Free_Languages.tex`          | `part_02_Foundations/chapter_06_ContextFreeLanguages/main.tex` — *разбивается*      |
| ↳                                     | `01_BasicDefinitions.tex`                                                           |
| ↳                                     | `02_EBNF.tex`                                                                       |
| ↳                                     | `03_RecursiveAutomata.tex`                                                          |
| ↳                                     | `04_DerivationTrees.tex`                                                            |
| ↳                                     | `05_SPPF.tex`                                                                       |
| ↳                                     | `06_CFLEmptiness.tex`                                                               |
| ↳                                     | `07_CNF.tex`                                                                        |
| ↳                                     | `08_PumpingLemma.tex`                                                               |
| ↳                                     | `09_ClosureProperties.tex`                                                          |
| `figures/cfl/*`                       | `part_02_Foundations/chapter_06_ContextFreeLanguages/figures/`                      |
| `ClassicalParsingAlgorithms.tex`      | `part_02_Foundations/chapter_07_ClassicalParsing/main.tex` — *разбивается*          |
| ↳                                     | `01_CYK.tex`                                                                        |
| ↳                                     | `02_Valiant.tex`                                                                    |
| ↳                                     | `03_FirstAndFollow.tex`                                                             |
| ↳                                     | `04_TopDown.tex`                                                                    |
| ↳                                     | `05_BottomUp.tex`                                                                   |
| ↳                                     | `06_LLvsLR.tex`                                                                     |
| `figures/cyk/graph1.tex`              | `part_02_Foundations/chapter_07_ClassicalParsing/figures/01_CYK/graph1.tex`         |
| `figures/GLR/CLR_example.tex`         | `figures/05_BottomUp/CLR_example.tex`                                               |
| `figures/GLR/GLR_example.tex`         | `figures/05_BottomUp/GLR_example.tex`                                               |
| `figures/GLR/LR0/*`                   | `figures/05_BottomUp/LR0/`                                                          |
| `figures/GLR/LL_LR.tex`               | `figures/06_LLvsLR/LL_LR.tex`                                                       |
| `Multiple_Context-Free_Languages.tex` | `part_02_Foundations/chapter_08_MCFG/main.tex` — *разбивается*                      |
| ↳                                     | `01_BasicDefinitions.tex`                                                           |
| ↳                                     | `02_NormalForm.tex`                                                                 |
| ↳                                     | `03_PumpingLemmas.tex`                                                              |
| ↳                                     | `04_Hierarchy.tex`                                                                  |
| ↳                                     | `05_ClosureProperties.tex`                                                          |
| `figures/mcfg/*`                      | `part_02_Foundations/chapter_08_MCFG/figures/`                                      |
| `ConjunctiveAndBooleanLanguages.tex`  | `part_02_Foundations/chapter_09_ConjunctiveBoolean/main.tex`                        |

### Часть 3. Анализ графов

| Старый файл                                       | Новый файл                                                                  |
| ------------------------------------------------- | --------------------------------------------------------------------------- |
| *— не существует*                                 | `part_03_GraphAnalysis/main.tex`                                            |
| `FLPQ.tex`                                        | `part_03_GraphAnalysis/chapter_10_FLPQ/main.tex` — *разбивается*            |
| ↳                                                 | `01_ProblemStatement.tex`                                                   |
| ↳                                                 | `02_Decidability.tex`                                                       |
| ↳                                                 | `03_SolutionRepresentation.tex`                                             |
| ↳                                                 | `04_RegularConstraints.tex`                                                 |
| ↳                                                 | `05_CFConstraints.tex`                                                      |
| ↳                                                 | `06_MCFGConstraints.tex`                                                    |
| `figures/flpq/*`                                  | `part_03_GraphAnalysis/chapter_10_FLPQ/figures/`                            |
| `RPQ.tex`                                         | `part_03_GraphAnalysis/chapter_11_RPQ/main.tex` — *разбивается*             |
| ↳                                                 | `01_TensorProduct.tex`                                                      |
| ↳                                                 | `02_BFS.tex`                                                                |
| ↳                                                 | `03_Arroyuelo.tex`                                                          |
| ↳                                                 | `04_Comparison.tex`                                                         |
| *— не существует*                                 | `part_03_GraphAnalysis/chapter_12_CFPQ/main.tex` *(вводная)*                |
| `CYK_for_CFPQ.tex`                                | `01_Hellings.tex`                                                           |
| `Matrix-based_CFPQ.tex`                           | `02_MatrixBased.tex`                                                        |
| `TensorProduct.tex`                               | `03_TensorProduct.tex`                                                      |
| `Matrix-based_CFPQ_MultipleSource.tex`            | `04_MatrixMultiSource.tex`                                                  |
| `TensorProduct_MultipleSource.tex`                | `05_TensorMultiSource.tex`                                                  |
| `GLL-based_CFPQ.tex`                              | `06_GLL_Based.tex`                                                          |
| `GLR-based_CFPQ.tex`                              | `07_GLR_Based.tex`                                                          |
| `CombinatorsForCFPQ.tex`                          | `08_Combinators.tex`                                                        |
| `figures/tensor/*`                                | `figures/03_TensorProduct/`                                                 |
| `figures/multi/graph0.tex`                        | `figures/04_MatrixMultiSource/graph0.tex`                                   |
| `figures/gll/*`                                   | `figures/06_GLL_Based/`                                                     |
| `CFPQ_Comparison.tex`                             | `part_03_GraphAnalysis/chapter_13_CFPQ_Comparison/main.tex` — *разбивается* |
| ↳                                                 | `01_ExperimentalStudy.tex`                                                  |
| ↳                                                 | `02_AlgorithmComparison.tex`                                                |
| *— не существует*                                 | `part_03_GraphAnalysis/chapter_14_BeyondCFL/main.tex` *(вводная)*           |
| `Multiple_Context-Free_Language_Reachability.tex` | `01_MCFGReachability.tex`                                                   |
| *— не существует*                                 | `02_ConjunctiveBooleanReachability.tex`                                     |

### Часть 4. Заключение

| Старый файл       | Новый файл                                          |
| ----------------- | --------------------------------------------------- |
| *— не существует* | `part_04_Conclusion/main.tex`                       |
| `Conclusion.tex`  | `part_04_Conclusion/chapter_15_Conclusion/main.tex` |

### Файлы к удалению

| Файл                  | Причина         |
| --------------------- | --------------- |
| `figures/Chomsky.pdf` | Не используется |
| `figures/Chomsky.svg` | Не используется |

---

## Итоговая структура директорий

```
tex/
├── FormalLanguageConstrainedReachabilityLectureNotes.tex
├── FormalLanguageConstrainedReachabilityLectureNotes.bib
├── kaobook.cls, kao.sty, kaobiblio.sty, Makefile
│
├── styles/                                             (не меняется)
│   └── *.tex
│
├── figures/
│   └── externalized/                                   (не меняется)
│
├── frontmatter/
│   ├── Introduction.tex
│   └── List_of_contributors.tex
│
├── part_01_Prep/
│   ├── main.tex
│   ├── chapter_01_LinearAlgebra/
│   │   ├── main.tex
│   │   ├── 01_BinaryOperations.tex
│   │   ├── 02_Semigroup.tex
│   │   ├── 03_Monoid.tex
│   │   ├── 04_Group.tex
│   │   ├── 05_Semiring.tex
│   │   ├── 06_Ring.tex
│   │   ├── 07_MatricesAndVectors.tex
│   │   └── 08_AppliedAspects.tex
│   ├── chapter_02_SetTheory/
│   │   ├── main.tex
│   │   ├── 01_BasicDefinitions.tex
│   │   └── 02_Relations.tex
│   └── chapter_03_GraphTheoryIntro/
│       ├── main.tex
│       ├── 01_BasicDefinitions.tex
│       ├── 02_PathProblems.tex
│       ├── 03_PathAlgebra.tex
│       ├── 04_BFS.tex
│       └── figures/
│           ├── graph0.tex .. graph5.tex
│           ├── graph_BFS_1.tex, graph_BFS_2.tex, graph_BFS_3.tex
│           ├── graph_MS-BFS_1.tex, graph_MS-BFS_2.tex
│           └── path0.tex
│
├── part_02_Foundations/
│   ├── main.tex
│   ├── chapter_04_FormalLanguageTheoryIntro/
│   │   ├── main.tex
│   │   ├── 01_SetOperations.tex
│   │   ├── 02_Derivatives.tex
│   │   ├── 03_Recognizers.tex
│   │   ├── 04_Generators.tex
│   │   └── 05_LanguageClasses.tex
│   ├── chapter_05_RegularLanguages/
│   │   ├── main.tex
│   │   ├── 01_RegularExpressions.tex
│   │   ├── 02_FiniteAutomata.tex
│   │   ├── 03_DerivativesForRegex.tex
│   │   ├── 04_RegexToFA.tex
│   │   ├── 05_FAToRegex.tex
│   │   ├── 06_LinearGrammars.tex
│   │   ├── 07_PumpingLemma.tex
│   │   └── 08_ClosureProperties.tex
│   ├── chapter_06_ContextFreeLanguages/
│   │   ├── main.tex
│   │   ├── 01_BasicDefinitions.tex
│   │   ├── 02_EBNF.tex
│   │   ├── 03_RecursiveAutomata.tex
│   │   ├── 04_DerivationTrees.tex
│   │   ├── 05_SPPF.tex
│   │   ├── 06_CFLEmptiness.tex
│   │   ├── 07_CNF.tex
│   │   ├── 08_PumpingLemma.tex
│   │   ├── 09_ClosureProperties.tex
│   │   └── figures/
│   │       ├── pumping0.tex
│   │       ├── pumping1.tex
│   │       ├── pumping2.tex
│   │       └── tree0.tex
│   ├── chapter_07_ClassicalParsing/
│   │   ├── main.tex
│   │   ├── 01_CYK.tex
│   │   ├── 02_Valiant.tex
│   │   ├── 03_FirstAndFollow.tex
│   │   ├── 04_TopDown.tex
│   │   ├── 05_BottomUp.tex
│   │   ├── 06_LLvsLR.tex
│   │   └── figures/
│   │       ├── 01_CYK/
│   │       │   └── graph1.tex
│   │       ├── 05_BottomUp/
│   │       │   ├── CLR_example.tex
│   │       │   ├── GLR_example.tex
│   │       │   └── LR0/
│   │       │       ├── complete.tex
│   │       │       └── state0.tex .. state5.tex
│   │       └── 06_LLvsLR/
│   │           └── LL_LR.tex
│   ├── chapter_08_MCFG/
│   │   ├── main.tex
│   │   ├── 01_BasicDefinitions.tex
│   │   ├── 02_NormalForm.tex
│   │   ├── 03_PumpingLemmas.tex
│   │   ├── 04_Hierarchy.tex
│   │   ├── 05_ClosureProperties.tex
│   │   └── figures/
│   │       ├── mcfg.svg, mcfg.pdf
│   │       └── mcfg_2.svg, mcfg_2.pdf
│   └── chapter_09_ConjunctiveBoolean/
│       └── main.tex
│
├── part_03_GraphAnalysis/
│   ├── main.tex
│   ├── chapter_10_FLPQ/
│   │   ├── main.tex
│   │   ├── 01_ProblemStatement.tex
│   │   ├── 02_Decidability.tex
│   │   ├── 03_SolutionRepresentation.tex
│   │   ├── 04_RegularConstraints.tex
│   │   ├── 05_CFConstraints.tex
│   │   ├── 06_MCFGConstraints.tex
│   │   └── figures/
│   │       ├── path1.tex
│   │       └── path2.tex
│   ├── chapter_11_RPQ/
│   │   ├── main.tex
│   │   ├── 01_TensorProduct.tex
│   │   ├── 02_BFS.tex
│   │   ├── 03_Arroyuelo.tex
│   │   └── 04_Comparison.tex
│   ├── chapter_12_CFPQ/
│   │   ├── main.tex
│   │   ├── 01_Hellings.tex
│   │   ├── 02_MatrixBased.tex
│   │   ├── 03_TensorProduct.tex
│   │   ├── 04_MatrixMultiSource.tex
│   │   ├── 05_TensorMultiSource.tex
│   │   ├── 06_GLL_Based.tex
│   │   ├── 07_GLR_Based.tex
│   │   ├── 08_Combinators.tex
│   │   └── figures/
│   │       ├── 03_TensorProduct/
│   │       │   ├── graph0.tex .. graph5.tex
│   │       │   └── recursive.tex
│   │       ├── 04_MatrixMultiSource/
│   │       │   └── graph0.tex
│   │       └── 06_GLL_Based/
│   │           ├── complete.tex
│   │           └── state0.tex .. state8.tex
│   ├── chapter_13_CFPQ_Comparison/
│   │   ├── main.tex
│   │   ├── 01_ExperimentalStudy.tex
│   │   └── 02_AlgorithmComparison.tex
│   └── chapter_14_BeyondCFL/
│       ├── main.tex
│       ├── 01_MCFGReachability.tex
│       └── 02_ConjunctiveBooleanReachability.tex
│
└── part_04_Conclusion/
    ├── main.tex
    └── chapter_15_Conclusion/
        └── main.tex
```

---

## Зеркало старой структуры (историческое)
```
├── Chapter files — все .tex файлы в корне tex/
│   ├── Introduction.tex
│   ├── LinearAlgebra.tex
│   ├── SetTheory.tex
│   ├── GraphTheoryIntro.tex
│   ├── FormalLanguageTheoryIntro.tex
│   ├── RegularLanguages.tex
│   ├── Context-Free_Languages.tex
│   ├── ClassicalParsingAlgorithms.tex
│   ├── Multiple_Context-Free_Languages.tex
│   ├── FLPQ.tex
│   ├── RPQ.tex
│   ├── CFPQ_Overview.tex
│   ├── CYK_for_CFPQ.tex
│   ├── Matrix-based_CFPQ.tex
│   ├── TensorProduct.tex
│   ├── Matrix-based_CFPQ_MultipleSource.tex
│   ├── TensorProduct_MultipleSource.tex
│   ├── GLL-based_CFPQ.tex
│   ├── GLR-based_CFPQ.tex
│   ├── CombinatorsForCFPQ.tex
│   ├── CFPQ_Comparison.tex
│   ├── Multiple_Context-Free_Language_Reachability.tex
│   ├── Conclusion.tex
│   └── List_of_contributors.tex
│
├── figures/
│   ├── Chomsky.pdf, Chomsky.svg                    → удалить
│   ├── externalized/                               → без изменений
│   ├── cfl/           → chapter_06_ContextFreeLanguages/figures/
│   ├── cyk/           → chapter_07_ClassicalParsing/figures/01_CYK/
│   ├── flpq/          → chapter_10_FLPQ/figures/
│   ├── gll/           → chapter_12_CFPQ/figures/06_GLL_Based/
│   ├── GLR/           → chapter_07_ClassicalParsing/figures/
│   │   ├── CLR_example.tex, GLR_example.tex → figures/05_BottomUp/
│   │   ├── LL_LR.tex                        → figures/06_LLvsLR/
│   │   └── LR0/                             → figures/05_BottomUp/LR0/
│   ├── graph/         → chapter_03_GraphTheoryIntro/figures/
│   ├── mcfg/          → chapter_08_MCFG/figures/
│   ├── multi/         → chapter_12_CFPQ/figures/04_MatrixMultiSource/
│   └── tensor/        → chapter_12_CFPQ/figures/03_TensorProduct/
```

## Frontmatter - ⚠️

- ## Список авторов - `List_of_contributors.tex`- ⚠️
- ## Введение - `Introduction.tex` - ⚠️

---
## Часть 1. Предподготовка — ⚠️

### Глава 1. Некоторые понятия линейной алгебры — `LinearAlgebra.tex` — ⚠️

- ✅ Раздел "Бинарные операции и их свойства"
- ✅ Раздел "Полугруппа"
- ✅ Раздел "Моноид"
- ✅ Раздел "Группа"
- ✅ Раздел "Полукольцо"
- ✅ Раздел "Кольцо"
- ✅ Раздел "Матрицы и вектора"
- ❌ Раздел "Прикладные особенности"
  - Планируемое содержание раздела: Взгляд программиста: типы данных, не совсем честные алгебраические структуры ("просто лишь бы типизировалось"), GraphBLAS, разреженность, параллельность. Операции типа маски, map2 и так далее.
- Задачи
  - Добавить раздел "Прикладные особенности"
  - Наполнить раздел "Прикладные особенности" содержимым

### Глава 2. Некоторые понятия теории множеств — `SetTheory.tex` — ✅

- ✅ Раздел "Основные определения"
- ✅ Раздел "Отношения"

### Глава 3. Некоторые сведения из теории графов — `GraphTheoryIntro.tex` — ⚠️

- ⚠️ Раздел "Основные определения"
  - Задачи
    - Обобщённая матрица смежности
    - Добавить булевы декомпозицию
- ⚠️ Раздел "Задачи поиска путей"
- ⚠️ Раздел "Анализ путей в графе и линейная алгебра"
  - Планируемое содержание раздела: общие сведения об Algebraic Path Problems, примеры (транзитивное замыкание, APSP)
- ⚠️ Раздел "Обход графа в ширину"
- Задачи
  - В разделе "Задачи поиска путей" оставить только обсуждение различных постановок задач
  - Перестроить раздел "Анализ путей в графе и линейная алгебра".
  - Удалить раздел "Алгоритм Флойда-Уоршелла". Вынести важные части в другие разделы ("Задачи поиска путей" или "Анализ путей в графе и линейная алгебра")


## Часть 2. Подготовка — ⚠️

### Глава 4. Общие сведения теории формальных языков — `FormalLanguageTheoryIntro.tex` — ✅

- ✅ Раздел "Теоретико-множественные операции над языками"
- ✅ Раздел "Производные"
- ✅ Раздел "Распознователи"
- ✅ Раздел "Генераторы"
- ✅ Раздел "Классы языков"

### Глава 5. Регулярные языки — `RegularLanguages.tex` — ✅

- ✅ Раздел "Регулярные выражения"
- ✅ Раздел "Конечные автоматы"
- ✅ Раздел "Производные для регулярных выражений"
- ✅ Раздел "Построение конечного автомата по регулярному выражению"
- ✅ Раздел "Построение регулярного выражения по конечному автомату"
- ✅ Раздел "Лево(право)линейные грамматики"
- ✅ Раздел "Лемма о накачке"
- ✅ Раздел "Замкнутость регулярных языков относительно теоретико-множественных операций"

### Глава 6. Контекстно-свободные языки и грамматики — `Context-Free_Languages.tex` — ⚠️

- ✅ Раздел "Основные определения"
- ❌ Раздел "Расширенная форма Бэкуса-Наура"
- ✅ Раздел "Рекурсивные автоматы и сети"
- ⚠️ Раздел "Дерево вывода"
  - Задачи
    - Добавить определение дерева для EBNF. Добавить пример.
- ⚠️ Раздел "Сжатое представление леса разбора
  - Планируемое содержание раздела: определения, структура SPPF, бинаризованный SPPF ($O(n^3)$), пример для строки"
  - Задачи
    - Не выделять подраздел "Лес разбора как представление КС грамматики". Интегрировать его в текст раздела
    - Доработать содержимое
- ✅ Раздел "Пустота КС-языка"
- ✅ Раздел "Нормальная форма Хомского"
- ✅ Раздел "Лемма о накачке"
- ✅ Раздел "Замкнутость КС-языков относительно операций"

### Глава 7. Классические алгоритмы синтаксического анализа — `ClassicalParsingAlgorithms.tex` — ⚠️

- ⚠️ Вводная часть главы:  история вопроса, обзор, ссылки на Грюна и другие классические работы
- ⚠️ Раздел "Алгоритм CYK"
- ⚠️ Раздел "Алгоритм Валианта"
- ⚠️ Раздел "Построение множеств first и follow"
- ⚠️ Раздел "Нисходящий синтаксический анализ"
  - ⚠️ Подраздел "Рекурсивный спуск"
  - ⚠️ Подраздел "LL(k) алгоритм"
  - ⚠️ Подраздел "Обобщённый LL алгоритм"
- ⚠️ Раздел "Восходящий синтаксический анализ"
  - ⚠️ Подраздел "LR(0) алгоритм"
  - ⚠️ Подраздел "SLR(1) алгоритм"
  - ⚠️ Подраздел "CLR(1) алгоритм"
  - ⚠️ Подраздел "Обобщённый LR алгоритм"
- ⚠️ Раздел "Сравнение классов LL и LR"
- Задачи
  - Разнести примеры по соответствующим разделам и подразделам

### Глава 8. Многокомпонентные контекстно-свободные языки — `Multiple_Context-Free_Languages.tex` — ⚠️

- ⚠️ Раздел "Основные определения"
- ⚠️ Раздел "Примеры"
- ⚠️ Раздел "Разновидности MCFG"
- ⚠️ Раздел "Нормальная форма"
- ⚠️ Раздел "Леммы о накачке"
- ⚠️ Раздел "Иерархия"
- ⚠️ Раздел "Свойства замкнутости"
- ⚠️ Раздел "Языки MIX и On"
- Задачи
  - Реструктурировать: "Примеры" и "Языки MIX и On" объединить с "Основные определения". Просто как примеры тех самых определений. Как в первых главах.
  - Реструктурировать: "Разновидности MCFG" объединить с "Основные определения". Просто ещё пачка определений.
  - Перепроверить все факты и ссылки в главе.

### Глава 9. Конъюнктивные и булевы языки — `ConjunctiveAndBooleanLanguages.tex` — ❌
- Задачи:
  - Подключить файл к проекту, проанализировать его структуру
  - Проработать структуру

## Часть 3. Анализа графов с использованием формальных языков в качестве ограничений на пути — ⚠️

### Глава 10. Задача анализа графов с использованием формальных языков в качестве ограничений на пути — `FLPQ.tex` — ⚠️

- ✅ Раздел "Постановка задачи"
- ✅ Раздел "О разрешимости задачи"
- ❌ Раздел "О представимости решения"
  - Планируемое содержание раздела: Представление результата --- бинарное отношение, матрица, представление всех путей
- ⚠️ Раздел "Регулярные языки в качестве ограничений на пути"
  - Планируемое содержание раздела:
    - история вопроса, обзор, мотивация. Уточнение общей формальной постановки с учётом языка, сведение к пересечению двух конечных автоматов
    - Описание областей применения, графовые БД, GQL
    - Практические аспекты — параллелизация, разреженность графов, размеры запросов, инкрементальность
- ⚠️ Раздел "Контекстно-свободные языки в качестве ограничений на пути"
  - Планируемое содержание раздела:
    - История вопроса
    - Уточнение общей формальной постановки с учётом языка
    - Общая идея адаптации алгоритмов синтаксического анализа к графам — замена позиций в строке на вершины графа, конфликт типа shift-shift
    - Представление всех путей: SPPF
    - Описание областей применения, статический анализ кода, анализ происхождения данных, ...
    - Практические аспекты — параллелизация, разреженность графов, размеры запросов, инкрементальность
- ⚠️ Раздел "Многокомпонентные контекстно-свободные языки в качестве ограничений на пути"
  - Планируемое содержание раздела:
    - История вопроса, обзор
    - Уточнение общей формальной постановки с учётом языка
    - О разрешимости задачи и представлении ответа
    - Описание областей применения, статический анализ кода, ...
- Задачи
  - Возможно, что-то вынести из `RPQ.tex` в раздел "Регулярные языки в качестве ограничений на пути"
  - Возможно, что-то вынести из `Multiple_Context-Free_Language_Reachability.tex` в раздел "Многокомпонентные контекстно-свободные языки в качестве ограничений на пути"
  - Перенести из `CFPQ_Overview.tex` в раздел "Контекстно-свободные языки в качестве ограничений на пути"
  - Добавить раздел "О представимости решения"
  - Наполнить содержимым раздел "О представимости решения"
  - Текущий раздел "Области применения" разнести по разделам для конкретных классов языков.

### Глава 11. Регулярные языки в качестве ограничения на пути — `RPQ.tex` — ⚠️
- Раздел "Пересечение автоматов через тензорное произведение"

- Раздел "Алгоритм Diego Arroyuelo"

- Раздел "Алгоритм на основе BFS"
- ⚠️ Раздел "Пересечение автоматов через тензорное произведение" Алгоритм на основе классического тензорного произведения (для всех пар)
- ⚠️ Раздел "Алгоритм на основе BFS"
- ❌ Раздел "Алгоритм Diego Arroyuelo"
  - Планируемое содержание раздела:
    - Из статьи "Evaluating Regular Path Queries on Compressed Adjacency Matrices"
- ❌ Раздел "Сравнение алгоритмов"
  - Планируемое содержание раздела:
    - Описание набора данных, участников сравнения
    - время работы, память

 ### Глава 12. Контекстно-свободные языки в качестве ограничения на пути
- ⚠️ Вводная часть главы:  история вопроса, обзор, мотивация
  - ⚠️ Раздел "Алгоритм Хеллингса" — `CYK_for_CFPQ.tex` — ⚠️
    - Планируемое содержание раздела:
      - Описание алгоритма, связь с CYK
      - Псевдокод
      - Примеры
    - ⚠️ Подраздел "Свойства алгоритма"
      - Планируемое содержание раздела:
        - Схема доказательства корректности, оценки временной и пространственной сложности

- Раздел "Алгоритмы на основе произведения матриц для всех пар вершин" — `Matrix-based_CFPQ.tex` — ⚠️
  - ⚠️ Вводная часть главы:  история вопроса (базовая версия, Илья Муравьёв)
  - ⚠️ Раздел "Описание базового алгоритма"
  - ⚠️ Раздел "Пример работы базового алгоритма"
  - ⚠️ Раздел "Свойства базового алгоритма"
  - ❌ Раздел "Оптимизация базового алгоритма достижимости"
  - ❌ Раздел "Поиск всех путей через пост-обработку решения задачи достижимости"
  - ❌ Раздел "Пример поиска всех путей через пост-обработку решения задачи достижимости"


- Раздел "Алгоритм на основе тензорного произведения" — `TensorProduct.tex` — ⚠️
  - ⚠️ Вводная часть главы:  история вопроса, обзор, мотивация
  - ⚠️ Раздел "Описание алгоритма"
    - Планируемое содержание раздела:
      - Описание
      - Псевдокод
  - ⚠️ Раздел "Примеры"
  - ⚠️ Раздел "Свойства алгоритма"
    - Планируемое содержание раздела:
      - Схема доказательства корректности, оценки временной и пространственной сложности


- Раздел "Матричный алгоритм для нескольких источников" — `Matrix-based_CFPQ_MultipleSource.tex` — ❌
  - ❌ Вводная часть главы:  история вопроса, обзор, мотивация
  - ❌ Раздел "Описание алгоритма"
    - Планируемое содержание раздела:
      - Описание
      - Псевдокод
  - ❌ Раздел "Примеры"
  - ❌ Раздел "Свойства алгоритма"
    - Планируемое содержание раздела:
      - Схема доказательства корректности, оценки временной и пространственной сложности


- Раздел "Алгоритм для нескольких источников на основе рекурсивных автоматов и BFS" — `TensorProduct_MultipleSource.tex` — ❌
  - ❌ Вводная часть главы:  история вопроса, обзор, мотивация
  - ❌ Раздел "Описание алгоритма"
    - Планируемое содержание раздела:
      - Описание
      - Псевдокод
  - ❌ Раздел "Примеры"
  - ❌ Раздел "Свойства алгоритма"
    - Планируемое содержание раздела:
      - Схема доказательства корректности, оценки временной и пространственной сложности


- Раздел "Обобщённый нисходящий алгоритм для поиска путей с КС ограничениям" — `GLL-based_CFPQ.tex` — ⚠️
  - ⚠️ Вводная часть главы:  история вопроса, обзор, мотивация
  - ⚠️ Раздел "Описание алгоритма"
    - Планируемое содержание раздела:
      - Описание, Адаптация GLL: множественный shift по всем исходящим рёбрам (конфликт типа shift-shift), Модификации GLR (RNGLR, BRNGLR)
      - Псевдокод
  - ❌ Раздел "Примеры"
  - ❌ Раздел "Свойства алгоритма"


- Раздел "Обобщённый алгоритм для поиска путей с КС ограничениям" — `GLR-based_CFPQ.tex` — ⚠️
    - ⚠️ Вводная часть главы:  история вопроса, обзор, мотивация
    - ⚠️ Раздел "Описание алгоритма"
    - Планируемое содержание раздела:
        - Описание, Адаптация GLR: множественный shift по всем исходящим рёбрам (конфликт типа shift-shift), Модификации GLR (RNGLR, BRNGLR)
        - Псевдокод
    - ❌ Раздел "Примеры"
    - ❌ Раздел "Свойства алгоритма"


- Раздел "Комбинаторы парсеров для поиска путей с КС ограничениям" — `CombinatorsForCFPQ.tex` — ⚠️
  - ⚠️ Вводная часть главы:  история вопроса, обзор, мотивация
  - ⚠️ Раздел "Описание алгоритма"
    - Планируемое содержание раздела:
      - Описание
      - Псевдокод
  - ❌ Раздел "Примеры"
  - ❌ Раздел "Свойства алгоритма"

### Глава 13. Сравнение алгоритмов, использующих КС языки в качестве ограничений — `CFPQ_Comparison.tex` — ❌

- ❌ Вводная часть главы:  обзор, мотивация
- ❌ Раздел "Экспериментальное исследование алгоритмов КС-достижимости"
  - Планируемое содержание раздела:
    - Описание набора данных
    - Результаты экспериментов: время, память (таблицы, графики)
    - Анализ результатов
- ❌ Раздел "Сравнение алгоритмов КС-достижимости"
  - Планируемое содержание раздела:
    - Сравнение свойств
    - Возможность параллелизации — матричные методы легко, GLL/GLR сложнее
    - Рекомендации по выбору — от одного источника или для всех пар, необходимость всех путей или только достижимости, размер грамматики

## Глава 14. За пределами контекстно-свободных языков
- Раздел "Матричный алгоритм достижимости с ограничениями в виде многокомпонентных контекстно-свободных языков" — `Multiple_Context-Free_Language_Reachability.tex` — ⚠️
  - ⚠️ Вводная часть главы:  история вопроса, обзор, мотивация
  - ⚠️ Раздел "Описание алгоритма"
  - ⚠️ Раздел "Примеры"
  - ⚠️ Раздел "Свойства алгоритма"
- Раздел "Матричный алгоритм достижимости с ограничениями в виде конъюнктивных и булевых языков"

## Часть 4. Заключение — ❌
## Глава 15. Заключение — `Conclusion.tex` — ❌

- Планируемое содержание главы:
  - Дальнейшие направления
  - Открытые проблемы, задачи, вопросы — как теоретические, так и прикладные: существование субкубического алгоритма для КС-достижимости, инкрементальные алгоритмы, масштабирование и распределённые алгоритмы
  - Свежие работы и обзоры
  - Общие заключительные слова.
- Задачи
  - Пописать содержимое. Не выделять разделы и подразделы

# Материалы по достижимости с ограничениями в виде формальных языков
- Книга на русском. Язык изложения --- русский.
- Корневой файл: `tex/FormalLanguageConstrainedReachabilityLectureNotes.tex`

## Сборка
- Находясь в директории 'tex' запустить `latexmk -interaction=nonstopmode -shell-escape FormalLanguageConstrainedReachabilityLectureNotes.tex`
- Не собирай проект без особой необходимости. Это занимает много времени.

## Вёрстка
- Используем sidenote вместо footnote
- Используем sidecite вместо cite почти всегда.
- Используем неразрывные пробелы
  - перед тире: текст~--- текст
  - перед ссылками: текст~\cite{...}, текст~\sidecite{...}

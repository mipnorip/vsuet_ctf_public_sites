---
Title: Симметричное шифрование
Sort: 3
---

`Алгоритмы шифрования` с симметричным ключом используют одни и те же криптографические ключи для шифрования простого текста и расшифровки зашифрованного. При использовании **симметричного шифрования** все получатели сообщения должны иметь доступ к общему ключу.

На следующих иллюстрациях показано, как шифрование и расшифровка работают с `симметричными ключами и алгоритмами`, когда все стороны используют один и тот же общий ключ.

На первой иллюстрации симметричный ключ и алгоритм используются для преобразования сообщения из обычного текста в зашифрованный. На второй иллюстрации показан тот же **симметричный ключ и симметричный алгоритм**, который используется для обратного преобразования зашифрованного текста в обычный.                

   ![](https://docs.aws.amazon.com/images/crypto/latest/userguide/images/Symmetric_Key_Encryption_sm.png)

Одним из самых популярных блочных шифров является [расширенный стандарт шифрования](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) (Advanced Encryption Standard, `AES`). Этот блочный шифр поддерживает 128-, 192- и 256-разрядные ключи. `AES` часто используется в сочетании со [счётчиком с аутентификацией Галуа](https://en.wikipedia.org/wiki/Galois/Counter_Mode) (Galois/Counter Mode, `GCM`), которое известно как AES-GCM, с целью создания алгоритма аутентифицированного шифрования.

**`AES`** – это промышленный стандарт шифрования, используемый во всем мире. Его безопасность широко известна, а эффективные программные и аппаратные реализации широко доступны.
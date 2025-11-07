-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Generation Time: Lis 07, 2025 at 08:53 AM
-- Wersja serwera: 9.5.0
-- Wersja PHP: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `miasto`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `adresy`
--

CREATE TABLE `adresy` (
  `id` int NOT NULL,
  `adres` varchar(100) NOT NULL,
  `wspolrzedne` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Zrzut danych tabeli `adresy`
--

INSERT INTO `adresy` (`id`, `adres`, `wspolrzedne`) VALUES
(1, 'Targówka spacerowa 16C', '52.167702454689184, 21.592018607125254');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `organizatorzy`
--

CREATE TABLE `organizatorzy` (
  `id` int NOT NULL,
  `nazwa` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Zrzut danych tabeli `organizatorzy`
--

INSERT INTO `organizatorzy` (`id`, `nazwa`) VALUES
(1, 'Agnieszka Nowicka');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `rodzaje`
--

CREATE TABLE `rodzaje` (
  `id` int NOT NULL,
  `nazwa` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Zrzut danych tabeli `rodzaje`
--

INSERT INTO `rodzaje` (`id`, `nazwa`) VALUES
(1, 'Zawody w piciu mleczka');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wydarzenia`
--

CREATE TABLE `wydarzenia` (
  `id` int NOT NULL,
  `data_od` date NOT NULL,
  `data_do` date NOT NULL,
  `nazwa` varchar(200) NOT NULL,
  `tytul` varchar(100) NOT NULL,
  `opis` text NOT NULL,
  `id_org` int NOT NULL,
  `id_rodz` int NOT NULL,
  `id_adr` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Zrzut danych tabeli `wydarzenia`
--

INSERT INTO `wydarzenia` (`id`, `data_od`, `data_do`, `nazwa`, `tytul`, `opis`, `id_org`, `id_rodz`, `id_adr`) VALUES
(2, '2025-03-03', '2026-09-10', 'siema', 'elo', 'zawody w piciu mleczka ewki poziom miedzynarodowy', 1, 1, 1);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `adresy`
--
ALTER TABLE `adresy`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `organizatorzy`
--
ALTER TABLE `organizatorzy`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `rodzaje`
--
ALTER TABLE `rodzaje`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `wydarzenia`
--
ALTER TABLE `wydarzenia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_org` (`id_org`),
  ADD KEY `id_rodz` (`id_rodz`),
  ADD KEY `id_adr` (`id_adr`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `adresy`
--
ALTER TABLE `adresy`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `organizatorzy`
--
ALTER TABLE `organizatorzy`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `rodzaje`
--
ALTER TABLE `rodzaje`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `wydarzenia`
--
ALTER TABLE `wydarzenia`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `wydarzenia`
--
ALTER TABLE `wydarzenia`
  ADD CONSTRAINT `wydarzenia_ibfk_1` FOREIGN KEY (`id_org`) REFERENCES `organizatorzy` (`id`),
  ADD CONSTRAINT `wydarzenia_ibfk_2` FOREIGN KEY (`id_rodz`) REFERENCES `rodzaje` (`id`),
  ADD CONSTRAINT `wydarzenia_ibfk_3` FOREIGN KEY (`id_adr`) REFERENCES `adresy` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

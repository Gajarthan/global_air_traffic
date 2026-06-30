# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_01:33:03_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-06-30 01:33:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-30 01:33:03 UTC

- **124,502** saved flights
- **42,628** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **124,502** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,504,570.3 tonnes** estimated CO2 emissions
- **87,221,468 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5074 |
| 2 | SkyWest Airlines | 4627 |
| 3 | EJA | 2437 |
| 4 | IndiGo | 2364 |
| 5 | American Airlines | 1927 |
| 6 | Southwest Airlines | 1871 |
| 7 | ENY | 1565 |
| 8 | Delta Air Lines | 1483 |
| 9 | Lufthansa | 1336 |
| 10 | LATAM Airlines | 1122 |
| 11 | Vueling | 1105 |
| 12 | WIF | 1099 |
| 13 | AZU | 1046 |
| 14 | AXM | 991 |
| 15 | LXJ | 965 |
| 16 | Swiss International | 875 |
| 17 | All Nippon Airways | 839 |
| 18 | Alaska Airlines | 817 |
| 19 | easyJet | 794 |
| 20 | QLK | 780 |
| 21 | EJU | 776 |
| 22 | Cathay Pacific | 694 |
| 23 | AEE | 686 |
| 24 | VIV | 680 |
| 25 | Air France | 676 |
| 26 | United Airlines | 667 |
| 27 | CXK | 664 |
| 28 | MXY | 650 |
| 29 | JetBlue | 635 |
| 30 | GLO | 623 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106257 |
| 2 | 🇪🇸 ES | 8348 |
| 3 | 🇮🇳 IN | 7421 |
| 4 | 🇦🇺 AU | 7259 |
| 5 | 🇧🇷 BR | 6916 |
| 6 | 🇩🇪 DE | 6603 |
| 7 | 🇮🇹 IT | 6583 |
| 8 | 🇨🇦 CA | 6537 |
| 9 | 🇬🇧 GB | 5488 |
| 10 | 🇯🇵 JP | 5474 |
| 11 | 🇫🇷 FR | 4926 |
| 12 | 🇨🇴 CO | 4032 |
| 13 | 🇲🇽 MX | 3623 |
| 14 | 🇬🇷 GR | 3543 |
| 15 | 🇳🇴 NO | 3421 |
| 16 | 🇨🇭 CH | 3184 |
| 17 | 🇹🇷 TR | 2614 |
| 18 | 🇲🇾 MY | 2565 |
| 19 | 🇿🇦 ZA | 2047 |
| 20 | 🇵🇱 PL | 2043 |
| 21 | 🇳🇿 NZ | 2008 |
| 22 | 🇹🇭 TH | 1942 |
| 23 | 🇰🇷 KR | 1935 |
| 24 | 🇵🇭 PH | 1766 |
| 25 | 🇬🇹 GT | 1718 |
| 26 | 🇲🇦 MA | 1340 |
| 27 | 🇲🇪 ME | 1239 |
| 28 | 🇳🇱 NL | 1178 |
| 29 | 🇲🇴 MO | 1177 |
| 30 | 🇧🇸 BS | 1078 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2615 |
| 2 | Denver International Airport |  | US | 2105 |
| 3 | Tokyo International Airport |  | JP | 1808 |
| 4 | Indira Gandhi International Airport |  | IN | 1634 |
| 5 | Harry Reid International Airport |  | US | 1559 |
| 6 | Guaymaral Airport |  | CO | 1520 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1493 |
| 8 | Zurich Airport |  | CH | 1378 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1332 |
| 10 | La Aurora Airport |  | GT | 1326 |
| 11 | Frankfurt am Main International Airport |  | DE | 1289 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1228 |
| 13 | Chicago O'Hare International Airport |  | US | 1206 |
| 14 | Macau International Airport |  | MO | 1177 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1101 |
| 17 | Capua Airport |  | IT | 1060 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1040 |
| 19 | Madrid Barajas International Airport |  | ES | 1032 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1003 |
| 21 | Kuala Lumpur International Airport |  | MY | 997 |
| 22 | Congonhas Airport |  | BR | 971 |
| 23 | Charlotte/Douglas International Airport |  | US | 941 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 913 |
| 25 | Charles de Gaulle International Airport |  | FR | 905 |
| 26 | Bengaluru International Airport |  | IN | 893 |
| 27 | Malpensa International Airport |  | IT | 860 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 825 |
| 29 | Ninoy Aquino International Airport |  | PH | 819 |
| 30 | Daniel K Inouye International Airport |  | US | 798 |
| 31 | Barcelona International Airport |  | ES | 778 |
| 32 | Tenerife Norte Airport |  | ES | 767 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 761 |
| 34 | Calgary International Airport |  | CA | 735 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 729 |
| 36 | Seattle-Tacoma International Airport |  | US | 720 |
| 37 | Vitoria/Foronda Airport |  | ES | 719 |
| 38 | Amsterdam Airport Schiphol |  | NL | 715 |
| 39 | Scottsdale Airport |  | US | 715 |
| 40 | Viracopos International Airport |  | BR | 703 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 454 | 21m | 244 km | 1,911.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 323 | 24m | 225 km | 1,253.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 312 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 299 | 1h 10m | 770 km | 3,972.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 185 | 22m | 55 km | 175.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 176 | 20m | 99 km | 301.5 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 173 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 172 | 44m | 241 km | 714.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 156 | 18m | 144 km | 388.0 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 152 | 20m | 250 km | 656.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 145 | 1h 38m | 1,156 km | 2,892.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 144 | 1h 1m | 695 km | 1,726.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 142 | 1h 17m | 961 km | 2,353.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 136 | 1h 1m | 611 km | 1,434.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N491LP |  | Moreton Airpark (23AZ) | Glendale Regional Airport (KGEU) | 2026-06-30 00:09 UTC | 2026-06-30 01:33 UTC | 1h 23m |
| N370WA |  | North Perry Airport (KHWO) | Miami Executive Airport (KTMB) | 2026-06-30 00:33 UTC | 2026-06-30 01:32 UTC | 59m |
| MTU55 | MTU | Murfreesboro Municipal Airport (KMBT) | Birmingham-Shuttlesworth International Airport (KBHM) | 2026-06-30 00:24 UTC | 2026-06-30 01:31 UTC | 1h 6m |
| N971TA |  | John Wayne/Orange County Airport (KSNA) | Whiteman Airport (KWHP) | 2026-06-30 00:47 UTC | 2026-06-30 01:24 UTC | 37m |
| N333CT |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-06-30 00:31 UTC | 2026-06-30 01:24 UTC | 52m |
| N628SR |  | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-06-30 00:39 UTC | 2026-06-30 01:14 UTC | 35m |
| ATCK103 | ATC | Grand Junction Regional Airport (KGJT) | Blanding Municipal Airport (KBDG) | 2026-06-30 00:33 UTC | 2026-06-30 01:11 UTC | 38m |
| SCU42 | SCU | Sahoma Lake Airport (03OK) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-06-29 23:23 UTC | 2026-06-30 01:07 UTC | 1h 44m |
| N217AX |  | Twentynine Palms Self Airport (KNXP) | Twentynine Palms Self Airport (KNXP) | 2026-06-30 00:52 UTC | 2026-06-30 01:03 UTC | 11m |
| N361ME |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-06-30 00:08 UTC | 2026-06-30 01:03 UTC | 54m |
| EXU | EXU | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-30 00:41 UTC | 2026-06-30 01:01 UTC | 20m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-30 00:07 UTC | 2026-06-30 01:01 UTC | 53m |
| RSCU903 | RSC | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-06-30 00:45 UTC | 2026-06-30 01:01 UTC | 15m |
| BLVF | BLV | Chek Lap Kok International Airport (VHHH) | Chek Lap Kok International Airport (VHHH) | 2026-06-30 00:55 UTC | 2026-06-30 00:59 UTC | 4m |
| UPS5852 | UPS | Salt Lake City International Airport (KSLC) | Phoenix Sky Harbor International Airport (KPHX) | 2026-06-29 23:39 UTC | 2026-06-30 00:54 UTC | 1h 15m |
| KAL1608 | Korean Air | Gimpo International Airport (RKSS) | G 710 Airport (RK6D) | 2026-06-29 22:22 UTC | 2026-06-30 00:50 UTC | 2h 27m |
| TKR12 | TKR | WN33 (WN33) | Crown Creek Ranch Airport (57WA) | 2026-06-30 00:43 UTC | 2026-06-30 00:48 UTC | 5m |
| JAL373 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-06-29 23:41 UTC | 2026-06-30 00:48 UTC | 1h 6m |
| CGDIO | CGD | Chatham Kent Airport (CYCK) | Guelph Airport (CNC4) | 2026-06-30 00:04 UTC | 2026-06-30 00:47 UTC | 43m |
| EJA889 | EJA | Camarillo Airport (KCMA) | NV13 (NV13) | 2026-06-29 23:58 UTC | 2026-06-30 00:47 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

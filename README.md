# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_17:59:48_UTC-green)

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

**Latest saved flight:** 2026-06-11 17:59:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-11 17:59:48 UTC

- **108,360** saved flights
- **37,939** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **108,360** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,324,408.8 tonnes** estimated CO2 emissions
- **76,777,322 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4468 |
| 2 | SkyWest Airlines | 4062 |
| 3 | IndiGo | 2149 |
| 4 | EJA | 2087 |
| 5 | American Airlines | 1719 |
| 6 | Southwest Airlines | 1624 |
| 7 | ENY | 1349 |
| 8 | Delta Air Lines | 1284 |
| 9 | Lufthansa | 1234 |
| 10 | Vueling | 992 |
| 11 | LATAM Airlines | 959 |
| 12 | WIF | 953 |
| 13 | AXM | 917 |
| 14 | AZU | 885 |
| 15 | LXJ | 816 |
| 16 | Swiss International | 788 |
| 17 | All Nippon Airways | 751 |
| 18 | Alaska Airlines | 741 |
| 19 | QLK | 717 |
| 20 | easyJet | 700 |
| 21 | EJU | 691 |
| 22 | Cathay Pacific | 651 |
| 23 | AEE | 617 |
| 24 | VIV | 617 |
| 25 | Air France | 612 |
| 26 | United Airlines | 596 |
| 27 | MXY | 582 |
| 28 | CXK | 571 |
| 29 | Japan Airlines | 534 |
| 30 | AXB | 532 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 91153 |
| 2 | 🇪🇸 ES | 7441 |
| 3 | 🇮🇳 IN | 6769 |
| 4 | 🇦🇺 AU | 6480 |
| 5 | 🇧🇷 BR | 5968 |
| 6 | 🇩🇪 DE | 5828 |
| 7 | 🇮🇹 IT | 5805 |
| 8 | 🇨🇦 CA | 5682 |
| 9 | 🇯🇵 JP | 4929 |
| 10 | 🇬🇧 GB | 4604 |
| 11 | 🇫🇷 FR | 4322 |
| 12 | 🇨🇴 CO | 3740 |
| 13 | 🇲🇽 MX | 3237 |
| 14 | 🇬🇷 GR | 3074 |
| 15 | 🇳🇴 NO | 3001 |
| 16 | 🇨🇭 CH | 2762 |
| 17 | 🇲🇾 MY | 2353 |
| 18 | 🇹🇷 TR | 2105 |
| 19 | 🇿🇦 ZA | 1849 |
| 20 | 🇰🇷 KR | 1795 |
| 21 | 🇳🇿 NZ | 1794 |
| 22 | 🇹🇭 TH | 1779 |
| 23 | 🇵🇱 PL | 1771 |
| 24 | 🇵🇭 PH | 1586 |
| 25 | 🇬🇹 GT | 1555 |
| 26 | 🇲🇦 MA | 1194 |
| 27 | 🇲🇴 MO | 1137 |
| 28 | 🇳🇱 NL | 1069 |
| 29 | 🇲🇪 ME | 1046 |
| 30 | 🇭🇷 HR | 949 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2331 |
| 2 | Denver International Airport |  | US | 1830 |
| 3 | Tokyo International Airport |  | JP | 1632 |
| 4 | Indira Gandhi International Airport |  | IN | 1473 |
| 5 | Guaymaral Airport |  | CO | 1379 |
| 6 | Harry Reid International Airport |  | US | 1376 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1354 |
| 8 | Zurich Airport |  | CH | 1228 |
| 9 | Frankfurt am Main International Airport |  | DE | 1217 |
| 10 | La Aurora Airport |  | GT | 1197 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1165 |
| 12 | Macau International Airport |  | MO | 1137 |
| 13 | El Dorado International Airport |  | CO | 1132 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1086 |
| 15 | Chicago O'Hare International Airport |  | US | 1077 |
| 16 | Madrid Barajas International Airport |  | ES | 941 |
| 17 | Capua Airport |  | IT | 934 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 922 |
| 19 | Kuala Lumpur International Airport |  | MY | 922 |
| 20 | Salt Lake City International Airport |  | US | 919 |
| 21 | Charlotte/Douglas International Airport |  | US | 837 |
| 22 | Congonhas Airport |  | BR | 825 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 823 |
| 24 | Charles de Gaulle International Airport |  | FR | 818 |
| 25 | Bengaluru International Airport |  | IN | 817 |
| 26 | Malpensa International Airport |  | IT | 800 |
| 27 | Daniel K Inouye International Airport |  | US | 729 |
| 28 | Ninoy Aquino International Airport |  | PH | 728 |
| 29 | Tenerife Norte Airport |  | ES | 726 |
| 30 | Barcelona International Airport |  | ES | 711 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 706 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 704 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 699 |
| 34 | Amsterdam Airport Schiphol |  | NL | 659 |
| 35 | Don Mueang International Airport |  | TH | 650 |
| 36 | Vitoria/Foronda Airport |  | ES | 647 |
| 37 | Calgary International Airport |  | CA | 637 |
| 38 | Seattle-Tacoma International Airport |  | US | 622 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 620 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 610 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 571 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 397 | 21m | 244 km | 1,671.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 288 | 24m | 225 km | 1,117.3 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 281 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 263 | 1h 25m | 910 km | 4,127.1 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 250 | 1h 10m | 770 km | 3,321.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 217 | 26m | 275 km | 1,028.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 208 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 159 | 22m | 55 km | 151.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 152 | 14m | 154 km | 402.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 150 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 150 | 27m | 152 km | 392.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 132 | 1h 1m | 695 km | 1,582.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 130 | 44m | 241 km | 540.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 128 | 1h 43m | 1,423 km | 3,141.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 123 | 1h 17m | 961 km | 2,038.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N54466 |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-06-11 17:26 UTC | 2026-06-11 17:59 UTC | 33m |
| SHWK436 | SHW | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-06-11 15:28 UTC | 2026-06-11 17:58 UTC | 2h 29m |
| N6269Q |  | Trenton Mercer Airport (KTTN) | Malone Airport (NJ61) | 2026-06-11 17:39 UTC | 2026-06-11 17:57 UTC | 18m |
| RNGR711 | RNG | XS10 (XS10) | XS10 (XS10) | 2026-06-11 17:45 UTC | 2026-06-11 17:57 UTC | 11m |
| N1311Z |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-06-11 17:28 UTC | 2026-06-11 17:55 UTC | 26m |
| TRF526 | TRF | Addison Airport (KADS) | Mesquite Metro Airport (KHQZ) | 2026-06-11 17:32 UTC | 2026-06-11 17:54 UTC | 22m |
| BGA163J | BGA | Getafe Air Base (LEGT) | Hamburg-Finkenwerder Airport (EDHI) | 2026-06-11 14:56 UTC | 2026-06-11 17:52 UTC | 2h 55m |
| RYR1BW | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Propriano Airport (LFKO) | 2026-06-11 16:52 UTC | 2026-06-11 17:49 UTC | 56m |
| WZZ3384 | Wizz Air | John Paul II International Airport Kraków-Balice Airport (EPKK) | Puimoisson Airport (LFTP) | 2026-06-11 15:43 UTC | 2026-06-11 17:49 UTC | 2h 5m |
| TKR160 | TKR | Albuquerque International Sunport Airport (KABQ) | Happy Mountain Airport (NM41) | 2026-06-11 17:21 UTC | 2026-06-11 17:39 UTC | 18m |
| VJT518 | VJT | Quatro De Fevereiro Airport (FNLU) | HE13 (HE13) | 2026-06-11 09:54 UTC | 2026-06-11 17:38 UTC | 7h 43m |
| CPA3295 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-06-11 02:43 UTC | 2026-06-11 17:37 UTC | 14h 53m |
| AXLE11 | AXL | Enix Airport (OK51) | Enix Airport (OK51) | 2026-06-11 17:08 UTC | 2026-06-11 17:36 UTC | 28m |
| UBD438 | UBD | Dusseldorf International Airport (EDDL) | Isparta Airport (LTBM) | 2026-06-11 09:44 UTC | 2026-06-11 17:33 UTC | 7h 49m |
| XSR362 | XSR | Van Nuys Airport (KVNY) | Mesawood Airport (6CO2) | 2026-06-11 16:00 UTC | 2026-06-11 17:33 UTC | 1h 32m |
| N6854Y |  | KE80 (KE80) | Roswell Air Center Airport (KROW) | 2026-06-11 16:13 UTC | 2026-06-11 17:33 UTC | 1h 20m |
| TCMTS | TCM | Ataturk International Airport (LTBA) | Batumi International Airport (UGSB) | 2026-06-11 14:08 UTC | 2026-06-11 17:31 UTC | 3h 23m |
| CODE21 | COD | Enix Airport (OK51) | Lariat Ranch Airport (OK42) | 2026-06-11 17:02 UTC | 2026-06-11 17:31 UTC | 29m |
| N306PM |  | Martha's Vineyard Airport (KMVY) | Norwood Memorial Airport (KOWD) | 2026-06-11 17:11 UTC | 2026-06-11 17:30 UTC | 18m |
| PBR680 | PBR | Victoria International Airport (CYYJ) | Alert Bay Airport (CYAL) | 2026-06-11 16:37 UTC | 2026-06-11 17:29 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

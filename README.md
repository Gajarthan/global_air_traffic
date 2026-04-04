# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_23:12:02_UTC-green)

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

**Latest saved flight:** 2026-04-04 23:12:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 23:12:02 UTC

- **17,088** saved flights
- **8,977** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,088** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **213,859.8 tonnes** estimated CO2 emissions
- **12,397,672 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 762 |
| 2 | Ryanair | 689 |
| 3 | IndiGo | 481 |
| 4 | EJA | 327 |
| 5 | American Airlines | 318 |
| 6 | Southwest Airlines | 241 |
| 7 | Lufthansa | 238 |
| 8 | ENY | 232 |
| 9 | Vueling | 189 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 161 |
| 12 | Delta Air Lines | 147 |
| 13 | LXJ | 147 |
| 14 | All Nippon Airways | 141 |
| 15 | QLK | 137 |
| 16 | AZU | 130 |
| 17 | VIV | 128 |
| 18 | Swiss International | 124 |
| 19 | Alaska Airlines | 117 |
| 20 | United Airlines | 116 |
| 21 | Avianca | 111 |
| 22 | EJU | 109 |
| 23 | EDV | 108 |
| 24 | easyJet | 107 |
| 25 | Japan Airlines | 107 |
| 26 | AEE | 105 |
| 27 | AXB | 105 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | GLO | 99 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13733 |
| 2 | 🇮🇳 IN | 1470 |
| 3 | 🇪🇸 ES | 1400 |
| 4 | 🇦🇺 AU | 1214 |
| 5 | 🇧🇷 BR | 996 |
| 6 | 🇨🇴 CO | 889 |
| 7 | 🇩🇪 DE | 873 |
| 8 | 🇯🇵 JP | 862 |
| 9 | 🇮🇹 IT | 788 |
| 10 | 🇨🇦 CA | 766 |
| 11 | 🇬🇧 GB | 661 |
| 12 | 🇫🇷 FR | 610 |
| 13 | 🇲🇽 MX | 590 |
| 14 | 🇬🇷 GR | 461 |
| 15 | 🇨🇭 CH | 445 |
| 16 | 🇳🇿 NZ | 382 |
| 17 | 🇲🇾 MY | 369 |
| 18 | 🇿🇦 ZA | 350 |
| 19 | 🇳🇴 NO | 341 |
| 20 | 🇬🇹 GT | 335 |
| 21 | 🇵🇭 PH | 311 |
| 22 | 🇹🇷 TR | 309 |
| 23 | 🇰🇷 KR | 293 |
| 24 | 🇵🇱 PL | 239 |
| 25 | 🇹🇭 TH | 232 |
| 26 | 🇲🇦 MA | 210 |
| 27 | 🇧🇸 BS | 190 |
| 28 | 🇮🇩 ID | 178 |
| 29 | 🇲🇴 MO | 174 |
| 30 | 🇲🇪 ME | 173 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 416 |
| 2 | El Dorado International Airport |  | CO | 336 |
| 3 | Denver International Airport |  | US | 323 |
| 4 | Indira Gandhi International Airport |  | IN | 304 |
| 5 | Tokyo International Airport |  | JP | 299 |
| 6 | La Aurora Airport |  | GT | 236 |
| 7 | Harry Reid International Airport |  | US | 227 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 215 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 204 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 184 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 181 |
| 13 | Guaymaral Airport |  | CO | 180 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 15 | Macau International Airport |  | MO | 174 |
| 16 | Chicago O'Hare International Airport |  | US | 171 |
| 17 | Charlotte/Douglas International Airport |  | US | 162 |
| 18 | Bengaluru International Airport |  | IN | 162 |
| 19 | Madrid Barajas International Airport |  | ES | 156 |
| 20 | Congonhas Airport |  | BR | 154 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 152 |
| 22 | Tenerife Norte Airport |  | ES | 150 |
| 23 | Ninoy Aquino International Airport |  | PH | 143 |
| 24 | Salt Lake City International Airport |  | US | 138 |
| 25 | Daniel K Inouye International Airport |  | US | 136 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 27 | Reno/Tahoe International Airport |  | US | 134 |
| 28 | Malpensa International Airport |  | IT | 133 |
| 29 | Kuala Lumpur International Airport |  | MY | 131 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 31 | Vitoria/Foronda Airport |  | ES | 125 |
| 32 | Charles de Gaulle International Airport |  | FR | 124 |
| 33 | Miami International Airport |  | US | 122 |
| 34 | Barcelona International Airport |  | ES | 120 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 116 |
| 36 | Pune Airport |  | IN | 116 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 110 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 39 | Seattle-Tacoma International Airport |  | US | 110 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 78 | 14m | 114 km | 153.0 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 68 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 45 | 22m | 99 km | 77.1 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 44 | 16m | 206 km | 156.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 40 | 28m | 275 km | 189.5 t |
| 13 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 37 | 30m | 369 km | 235.5 t |
| 14 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 37 | 1h 54m | 1,304 km | 832.4 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 17 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 32 | 1h 43m | 1,423 km | 785.3 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 31 | 58m | 723 km | 386.5 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N35SD |  | Albany International Airport (KALB) | Lebanon Municipal Airport (KLEB) | 2026-04-04 22:25 UTC | 2026-04-04 23:12 UTC | 46m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-04-04 22:50 UTC | 2026-04-04 23:04 UTC | 13m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-04-04 11:22 UTC | 2026-04-04 22:49 UTC | 11h 27m |
| N817SD |  | Brown Field Municipal Airport (KSDM) | Scottsdale Airport (KSDL) | 2026-04-04 21:53 UTC | 2026-04-04 22:47 UTC | 53m |
| N616AW |  | Kansas City Downtown/Wheeler Field (KMKC) | Angle Bar M Airport (MU07) | 2026-04-04 22:22 UTC | 2026-04-04 22:45 UTC | 22m |
| N60DM |  | Salt Lake City International Airport (KSLC) | Big Bear City Airport (KL35) | 2026-04-04 20:09 UTC | 2026-04-04 22:43 UTC | 2h 33m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-04-04 10:46 UTC | 2026-04-04 22:38 UTC | 11h 51m |
| CXK437 | CXK | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-04-04 21:48 UTC | 2026-04-04 22:35 UTC | 46m |
| BRG682 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-04 22:07 UTC | 2026-04-04 22:34 UTC | 27m |
| CFOCI | CFO | Miami-Opa Locka Executive Airport (KOPF) | Laurence G Hanscom Field (KBED) | 2026-04-04 19:46 UTC | 2026-04-04 22:29 UTC | 2h 43m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-04-04 12:10 UTC | 2026-04-04 22:29 UTC | 10h 18m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-04 22:14 UTC | 2026-04-04 22:26 UTC | 12m |
| N178MP |  | KU42 (KU42) | Lava Hot Springs Airpark (01ID) | 2026-04-04 22:02 UTC | 2026-04-04 22:26 UTC | 24m |
| N927SJ |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-04-04 22:18 UTC | 2026-04-04 22:25 UTC | 7m |
| AAL1715 | American Airlines | Miami International Airport (KMIA) | St Louis Lambert International Airport (KSTL) | 2026-04-04 20:03 UTC | 2026-04-04 22:25 UTC | 2h 21m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-04 11:46 UTC | 2026-04-04 22:24 UTC | 10h 37m |
| GLO2050 | GLO | Galeao - Antonio Carlos Jobim International Airport (SBGL) | Fazenda Cedro Airport (SWCE) | 2026-04-04 20:20 UTC | 2026-04-04 22:23 UTC | 2h 2m |
| N49TT |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-04 21:26 UTC | 2026-04-04 22:22 UTC | 56m |
| N9378D |  | Santa Monica Municipal Airport (KSMO) | Van Nuys Airport (KVNY) | 2026-04-04 22:03 UTC | 2026-04-04 22:21 UTC | 17m |
| N7487G |  | Carter-Norman Airport (TA87) | Carter-Norman Airport (TA87) | 2026-04-04 22:20 UTC | 2026-04-04 22:20 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

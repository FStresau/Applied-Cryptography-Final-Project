# Final Project Report

## Hash Function Analysis  

**Prepared by:**  
Jacob Miller, Tyler Guthrie, Frederic Stresau, Jackson Harper, Quy Pham, Louis Irias  

**Course:**  
Applied Cryptography  
CIS 4362  

**Instructor:**  
Dr. Ujan Mukhopadhyay  

**Date:**  
4/16/2024  

---

## Problem Definition

In the realm of data security and integrity, the reliance on hash functions is paramount. A hash function converts an input (or "message") into a fixed-size string of bytes. These functions are extensively used in various applications such as digital signatures, data integrity verification, and password storage. Ensuring the reliability and robustness of hash functions is crucial for safeguarding sensitive information.

The objective of this project is to analyze and validate the properties of a hash function, focusing on four essential characteristics: **One-way property**, **Collision Resistance**, **Fixed Length**, and **Determinism**.

---

## Methodology

To begin our methodology, it is crucial to fully understand the four essential characteristics that the hash function needs to exhibit:

- **One-way Property:**  
  The hash function must be computationally infeasible to invert. This ensures data confidentiality and prevents unauthorized access.

- **Collision Resistance:**  
  A robust hash function should minimize the likelihood of collisions, which is critical for applications like digital signatures and certificate authorities.

- **Fixed Length:**  
  Hash values must have a fixed length regardless of the input size, ensuring efficiency in storage and transmission.

- **Determinism:**  
  The hash function must produce consistent results for the same input, ensuring reliability across systems.

After analyzing these characteristics, we selected **HAVAL** as the hash function of choice for this project.

---

## Discussion of Findings

### 1.0 HAVAL Essential Characteristics

**HAVAL** is a cryptographic hash function designed to meet stringent security requirements. Below is an analysis of how it satisfies key properties:

#### 1.1 One-Way Property  
HAVAL is computationally infeasible to reverse. This is achieved through complex operations and transformations, such as non-linear functions and bitwise operations running through multiple rounds of processing (3-5 rounds). These features make it resistant to attacks.

#### 1.2 Determinism  
HAVAL consistently produces the same hash value for identical inputs. This ensures predictability, with fixed initialization values and consistent algorithmic steps ensuring reliability.

#### 1.3 Collision Resistance  
HAVAL minimizes collision probability using multiple processing rounds (3, 4, or 5) and output lengths of 128, 160, 192, 224, or 256 bits. Increased rounds and longer output sizes significantly reduce collision likelihood.

#### 1.4 Fixed Length  
HAVAL generates fixed-length hash values for its variants (e.g., HAVAL-256). The algorithm uses padding to standardize input lengths, followed by processing in blocks and a compression function to produce the fixed-length output.

---

## HAVAL Functional Analysis

HAVAL processes 1024-bit blocks to generate fixed-length outputs (128–256 bits). Key steps include:

- **Padding and Block Assembly:**  
  Messages are padded to 1024-bit blocks with metadata fields (e.g., VERSION, PASS, FPTLEN, MSGLEN).

- **Compression Algorithm:**  
  The algorithm processes blocks in multiple passes (H1 through H5), with each pass applying 32 rounds of unique operations to enhance security.

Key operational properties include:  
- **0-1 Balanced Output:** Ensures equal probability for 0 and 1 bits in the output.  
- **High Non-Linearity:** Prevents linear relationships between input and output.  
- **Strict Avalanche Criterion (SAC):** A single-bit change in input causes drastic output changes.  

HAVAL employs 136 constant 32-bit words derived from Pi for its operations.

---

## Breaking HAVAL and Vulnerabilities

In 2004, researchers Xiaoyun Wang, Dengguo Feng, Xuejia Lai, and Hongbo Yu identified collisions in HAVAL-128. They demonstrated that full HAVAL-128 could be broken with only ~2^6 computations, highlighting vulnerabilities in the algorithm.

---

## Resources

- Aurora, Valerie. *Lifetimes of Cryptographic Hash Functions.*  
  [valerieaurora.org/hash.html](http://valerieaurora.org/hash.html)  

- Wikipedia. *HAVAL.*  
  [en.wikipedia.org/wiki/HAVAL](https://en.wikipedia.org/wiki/HAVAL#cite_note-1)  

- Schneier, Bruce. *Chapter 18 - One-Way Hash Functions.* Applied Cryptography. John Wiley & Sons.  

- Sklavos, Nicolas, and C. Efstathiou. *On the FPGA Implementation of HAVAL Hash Function.*  
  [ResearchGate Article](https://www.researchgate.net/publication/224633911_On_the_FPGA_implementation_of_HAVAL_hash_function)  

- Wang, X., Feng, D., Lai, X., & Yu, H. *Collisions for Hash Functions MD4, MD5, HAVAL-128, and RIPEMD.*  
  [Cryptology ePrint Archive](https://eprint.iacr.org/2004/199.pdf)  

- Zheng, Y., Pieprzyk, J., & Seberry, J. *HAVAL — A One-Way Hashing Algorithm with Variable Length Output.*  

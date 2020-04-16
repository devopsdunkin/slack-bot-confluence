\MAKEFLAGS -= --silent

define encrypt
	gcloud kms encrypt \
		--project hy-vee-kms \
		--location us-central1 \
		--keyring systems \
		--key infrastructure \
		--ciphertext-file "$(1).kms" \
		--plaintext-file "$(1)"
endef

define decrypt
	gcloud kms decrypt \
		--project hy-vee-kms \
		--location us-central1 \
		--keyring systems \
		--key infrastructure \
		--ciphertext-file "$(1).kms" \
		--plaintext-file "$(1)"
endef